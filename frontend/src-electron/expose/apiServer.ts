import { type ChildProcess, spawn } from 'child_process';
import path from 'path';

let serverProcess: ChildProcess | undefined;

export default {
  /**
   * Start the API server.
   *
   * @returns {ChildProcess} The server process.
   */
  async start(): Promise<ChildProcess> {
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
  async stop(): Promise<boolean> {
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
    await this.stop();
    return new Promise((resolve) => {
      setTimeout(async () => {
        resolve(await this.start());
      }, 2500);
    });
  },

  serverProcess,
};
