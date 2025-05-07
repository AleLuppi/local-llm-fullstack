import { app, BrowserWindow } from 'electron';
import { initialize, enable } from '@electron/remote/main/index.js';
import path from 'path';
import os from 'os';
import { fileURLToPath } from 'url';
import apiServer from './expose/apiServer';

// Enable electron remote module
initialize();

// Needed in case process is undefined under Linux
const platform = process.platform || os.platform();

const currentDir = fileURLToPath(new URL('.', import.meta.url));

let mainWindow: BrowserWindow | undefined;

async function createWindow() {
  /**
   * Initial window options
   */
  mainWindow = new BrowserWindow({
    icon: path.resolve(currentDir, 'icons/icon.png'), // tray icon
    width: 1000,
    height: 600,
    useContentSize: true,
    frame: false,
    webPreferences: {
      contextIsolation: true,
      sandbox: false, // to be able to import @electron/remote in preload script
      // More info: https://v2.quasar.dev/quasar-cli-vite/developing-electron-apps/electron-preload-script
      preload: path.resolve(
        currentDir,
        path.join(
          process.env.QUASAR_ELECTRON_PRELOAD_FOLDER,
          'electron-preload' + process.env.QUASAR_ELECTRON_PRELOAD_EXTENSION,
        ),
      ),
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

  // Load and display splash screen while loading main window
  splashWindow.loadFile(
    path.resolve(process.env.DEV ? 'src-electron' : process.resourcesPath, 'splash.html'),
  );
  splashWindow.center();

  enable(mainWindow.webContents);

  if (process.env.DEV) {
    await mainWindow.loadURL(process.env.APP_URL);
  } else {
    await mainWindow.loadFile('index.html');
  }

  // App is now loaded: destroy splash window and start the API server
  splashWindow.close();
  if (process.env.PROD) apiServer.start();

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

void app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (platform !== 'darwin') {
    app.quit();
  }

  void apiServer.stop();
});

app.on('activate', () => {
  if (mainWindow === undefined) {
    void createWindow();
  }
});
