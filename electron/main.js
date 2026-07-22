// ARIA MAX — Electron desktop shell (turns the app into a real Windows/macOS program)
// Build:  cd electron && npm init -y && npm i -D electron electron-builder
//         npx electron .                      → run as a desktop app now
//         npx electron-builder --win portable → build ARIA-INFINITY.exe (see package-example.json)
const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 1360,
    height: 860,
    backgroundColor: '#04060e',
    autoHideMenuBar: true,
    icon: path.join(__dirname, '..', 'icon.svg'),
    webPreferences: { spellcheck: false }
  });
  win.loadFile(path.join(__dirname, '..', 'index.html'));
}

app.whenReady().then(() => {
  createWindow();
  app.on('activate', () => { if (BrowserWindow.getAllWindows().length === 0) createWindow(); });
});
app.on('window-all-closed', () => { if (process.platform !== 'darwin') app.quit(); });
