#!/usr/bin/env python3
"""ARIA MAX app server — HTTPS server for local PC & mobile devices.

Usage:  python serve.py [port]     (default 8323)

- Serves over HTTPS so iOS Safari unlocks full microphone access (getUserMedia).
- /myip endpoint lets the app render a QR code your phone can scan.
"""
import ipaddress, json, os, socket, sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

ROOT = os.path.dirname(os.path.abspath(__file__))

class H(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        if self.path in ('/', '/index.html') or self.path.endswith('.html'):
            self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def do_GET(self):
        if self.path.split('?')[0] == '/myip':
            ip = lan_ip()
            body = json.dumps({'ip': ip}).encode()
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def log_message(self, *a):
        pass

def lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return 'localhost'

def ensure_cert():
    cert_file = os.path.join(ROOT, 'cert.pem')
    key_file = os.path.join(ROOT, 'key.pem')
    if os.path.exists(cert_file) and os.path.exists(key_file):
        return cert_file, key_file
    try:
        import datetime
        from cryptography import x509
        from cryptography.x509.oid import NameOID
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import rsa

        ip = lan_ip()
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, u"aria-max.local"),
        ])
        alt_names = [x509.DNSName(u"localhost")]
        try:
            alt_names.append(x509.IPAddress(ipaddress.ip_address(ip)))
        except Exception:
            pass

        cert = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.datetime.now(datetime.timezone.utc)
        ).not_valid_after(
            datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=3650)
        ).add_extension(
            x509.SubjectAlternativeName(alt_names),
            critical=False,
        ).sign(key, hashes.SHA256())

        with open(key_file, "wb") as f:
            f.write(key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))
        with open(cert_file, "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
        return cert_file, key_file
    except Exception as e:
        print(f"Notice: SSL cert generation fallback ({e})")
        return None, None

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8323
    ip = lan_ip()
    cert_file, key_file = ensure_cert()
    httpd = ThreadingHTTPServer(('0.0.0.0', port), H)

    if cert_file and key_file:
        import ssl
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ctx.load_cert_chain(certfile=cert_file, keyfile=key_file)
        httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
        proto = "https"
    else:
        proto = "http"

    print(f'ARIA MAX {proto.upper()} server is running (Ctrl+C to stop).')
    print(f'  This PC:     {proto}://localhost:{port}')
    print(f'  Your phone:  {proto}://{ip}:{port}   (same Wi-Fi — opens with full microphone access!)')
    httpd.serve_forever()
