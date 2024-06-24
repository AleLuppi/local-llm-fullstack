// Extend the default window object with new api methods
interface Window {
  apiWindow: ApiWindow;
}

interface ApiWindow {
  minimize: () => void;
  toggleMaximize: () => void;
  close: () => void;
}
