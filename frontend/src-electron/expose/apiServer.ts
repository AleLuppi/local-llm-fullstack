import { type ChildProcess, spawn } from 'child_process';
import path from 'path';

let serverProcess: ChildProcess | undefined;

export default {
  /**
   * Start the API server.
   *
   * @returns {ChildProcess} The server process.
   */
  start(): ChildProcess {
    serverProcess = spawn(
      path.resolve(
        process.env.APP_SERVER_LOCAL_PATH ?? 'server',
        process.env.APP_API_NAME + '.exe',
      ),
    );

    return serverProcess;
  },

  /**
   * Stop the API server.
   *
   * @returns {boolean} True if server was successfully killed.
   */
  stop(): boolean {
    const killed = serverProcess?.kill() ?? false;
    serverProcess = undefined;
    return killed;
  },

  /**
   * Restart the API server.
   *
   * @returns {ChildProcess} The server process.
   */
  async restart(): Promise<ChildProcess> {
    this.stop();
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(this.start());
      }, 2500);
    });
  },

  serverProcess,
};
