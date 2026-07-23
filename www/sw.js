/* ARIA MAX service worker — network-first shell (updates always reach you), cache = offline fallback */
const CACHE = 'aria-max-v1';
const ASSETS = ['./', './index.html', './manifest.json', './icon.svg',
  './vendor/three.min.js', './vendor/qrcode.min.js', './vendor/jspdf.min.js',
  './vendor/inter-400.woff2', './vendor/inter-600.woff2', './vendor/inter-700.woff2'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if (url.origin !== location.origin) return;          // never touch AI / sync calls
  if (url.pathname.endsWith('/myip')) return;          // always live

  const isShell = e.request.mode === 'navigate' || url.pathname.endsWith('/index.html') || url.pathname.endsWith('/');
  if (isShell) {
    e.respondWith(
      fetch(e.request).then(res => {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(e.request, copy));
        return res;
      }).catch(() => caches.match(e.request).then(hit => hit || caches.match('./index.html')))
    );
    return;
  }
  e.respondWith(
    caches.match(e.request).then(hit => hit ||
      fetch(e.request).then(res => {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(e.request, copy));
        return res;
      }).catch(() => caches.match('./index.html'))
    )
  );
});

/* Background Notification Scheduler for PWA & iOS */
self.addEventListener('notificationclick', e => {
  e.notification.close();
  e.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then(clientList => {
      if (clientList.length > 0) return clientList[0].focus();
      return clients.openWindow('./index.html');
    })
  );
});

self.addEventListener('message', e => {
  if (e.data && e.data.type === 'SCHEDULE_NOTIFICATION') {
    const { title, body, delayMs, id } = e.data;
    setTimeout(() => {
      self.registration.showNotification(title, {
        body,
        icon: './icon.svg',
        tag: id,
        renotify: true,
        vibrate: [200, 100, 200, 100, 400]
      });
    }, Math.max(0, delayMs));
  }
});
