import { BrowserWindow } from '@electron/remote';

export default {
  /**
   * Minimizes the app window.
   */
  minimize() {
    BrowserWindow.getFocusedWindow()?.minimize();
  },

  /**
   * Toggles the app window's maximize state.
   */
  toggleMaximize() {
    const win = BrowserWindow.getFocusedWindow();
    if (!win) return;

    if (win.isMaximized()) {
      win.unmaximize();
    } else {
      win.maximize();
    }
  },

  /**
   * Closes the app window.
   */
  close() {
    BrowserWindow.getFocusedWindow()?.close();
  },
};
