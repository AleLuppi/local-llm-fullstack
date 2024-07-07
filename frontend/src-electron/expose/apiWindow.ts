import { BrowserWindow } from '@electron/remote';

export default {
  /**
   * Minimizes the app window.
   *
   * @returns {boolean} True when minimized.
   */
  minimize(): true | undefined {
    const win = BrowserWindow.getFocusedWindow();

    if (win) {
      win.minimize();
      return true;
    }
  },

  /**
   * Toggles the app window's maximize state.
   *
   * @returns {boolean} True when maximized, false when unmaximized.
   */
  toggleMaximize(): boolean | undefined {
    const win = BrowserWindow.getFocusedWindow();
    if (!win) return;

    if (win.isMaximized()) {
      win.unmaximize();
      return false;
    } else {
      win.maximize();
      return true;
    }
  },

  /**
   * Closes the app window.
   *
   * @returns {boolean} True when closed.
   */
  close(): true | undefined {
    const win = BrowserWindow.getFocusedWindow();

    if (win) {
      win.close();
      return true;
    }
  },
};
