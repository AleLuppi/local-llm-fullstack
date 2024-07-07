// Extend the default window object with new api methods
interface Window {
  apiWindow: ApiWindow;
  apiServer: ApiServer;
}

interface ApiWindow {
  minimize: () => true | undefined;
  toggleMaximize: () => boolean | undefined;
  close: () => true | undefined;
}

interface ApiServer {
  start: () => Promise<import('child_process').ChildProcess>;
  stop: () => Promise<boolean>;
  restart: () => Promise<import('child_process').ChildProcess>;
}
