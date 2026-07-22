#!/usr/bin/env python3
"""ARIA X LAN sync server — runs on YOUR computer. Zero cloud.

Usage:  python sync-server.py [port]     (default 8765)

Put your PC and phone on the same Wi-Fi, run this, then in ARIA X on BOTH
devices: Settings -> Device sync -> paste the printed URL -> "Sync now".
The merged snapshot is stored in aria-sync.json next to this file.
"""
import json, os, socket, sys
from http.server import HTTPServer, BaseHTTPRequestHandler

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aria-sync.json')

class H(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'content-type')

    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()

    def do_GET(self):
        path = self.path.split('?')[0].rstrip('/')
        if path == '':
            body = b'ARIA X sync server is running. Point ARIA X Settings -> Device sync here.'
            self.send_response(200); self._cors()
            self.send_header('content-type', 'text/plain'); self.end_headers()
            self.wfile.write(body); return
        if path == '/data':
            data = b'{}'
            if os.path.exists(FILE):
                with open(FILE, 'rb') as f: data = f.read()
            self.send_response(200); self._cors()
            self.send_header('content-type', 'application/json'); self.end_headers()
            self.wfile.write(data); return
        self.send_response(404); self._cors(); self.end_headers()

    def do_POST(self):
        if self.path.split('?')[0].rstrip('/') == '/data':
            n = int(self.headers.get('content-length', 0))
            raw = self.rfile.read(n)
            try:
                json.loads(raw)
            except Exception:
                self.send_response(400); self._cors(); self.end_headers(); return
            with open(FILE, 'wb') as f: f.write(raw)
            self.send_response(200); self._cors()
            self.send_header('content-type', 'application/json'); self.end_headers()
            self.wfile.write(b'{"ok":true}'); return
        self.send_response(404); self._cors(); self.end_headers()

    def log_message(self, *a):
        pass

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    ip = 'localhost'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80)); ip = s.getsockname()[0]; s.close()
    except Exception:
        pass
    print('ARIA X sync server running (Ctrl+C to stop).')
    print(f'  On this PC:     http://localhost:{port}')
    print(f'  On your phone:  http://{ip}:{port}   (same Wi-Fi)')
    print('Paste that URL in ARIA X -> Settings -> Device sync on BOTH devices, then press "Sync now" on each.')
    HTTPServer(('0.0.0.0', port), H).serve_forever()
