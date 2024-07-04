import { app, BrowserWindow } from 'electron';
import { initialize, enable } from '@electron/remote/main';
import path from 'path';
import os from 'os';
import apiServer from './expose/apiServer';

// Enable electron remote module
initialize();

// Needed in case process is undefined under Linux
const platform = process.platform || os.platform();

let mainWindow: BrowserWindow | undefined;

function createWindow() {
  // Initial window options
  mainWindow = new BrowserWindow({
    icon: path.resolve(__dirname, 'icons/icon.png'), // tray icon
    width: 1000,
    height: 600,
    useContentSize: true,
    frame: false,
    webPreferences: {
      contextIsolation: true,
      sandbox: false, // to be able to import @electron/remote in preload script
      // More info: https://v2.quasar.dev/quasar-cli-vite/developing-electron-apps/electron-preload-script
      preload: path.resolve(__dirname, process.env.QUASAR_ELECTRON_PRELOAD),
    },
  });

  // Initial splash window options
  const splashWindow = new BrowserWindow({
    width: 300,
    height: 300,
    transparent: true,
    frame: false,
    alwaysOnTop: false,
  });

  // FIXME Load and display splash screen while loading main window
  // splashWindow.loadFile(
  // );
  splashWindow.center();

  enable(mainWindow.webContents);

  // Load main window, thus close splash screen
  mainWindow.loadURL(process.env.APP_URL).then(() => {
    splashWindow.close();
    mainWindow?.show();

    // Immediately start the API server
    apiServer.start();
  });

  // Disable dev tools in production
  if (process.env.DEBUGGING) {
    // if on DEV or Production with debug enabled
    mainWindow.webContents.openDevTools();
  } else {
    // we're on production; no access to devtools pls
    mainWindow.webContents.on('devtools-opened', () => {
      mainWindow?.webContents.closeDevTools();
    });
  }

  mainWindow.on('closed', () => {
    mainWindow = undefined;
  });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (platform !== 'darwin') {
    app.quit();
  }

  apiServer.stop();
});

app.on('activate', () => {
  if (mainWindow === undefined) {
    createWindow();
  }
});
