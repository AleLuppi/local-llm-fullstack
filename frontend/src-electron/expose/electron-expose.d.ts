import type { default as ApiWindow } from './apiWindow';
import type { default as ApiServer } from './apiServer';

// Extend the default window object with new api methods
declare global {
  interface Window {
    apiWindow: typeof ApiWindow;
    apiServer: typeof ApiServer;
  }
}
