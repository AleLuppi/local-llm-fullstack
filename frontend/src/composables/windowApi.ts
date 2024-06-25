export function useWindowApi() {
  /**
   * Minimizes the app window.
   */
  function minimize() {
    if (process.env.MODE === 'electron') {
      window.apiWindow.minimize();
    }
  }

  /**
   * Toggles the app window's maximize state.
   */
  function toggleMaximize() {
    if (process.env.MODE === 'electron') {
      window.apiWindow.toggleMaximize();
    }
  }

  /**
   * Closes the app window.
   */
  function closeApp() {
    if (process.env.MODE === 'electron') {
      window.apiWindow.close();
    }
  }

  return {
    minimize,
    toggleMaximize,
    closeApp,
  };
}
