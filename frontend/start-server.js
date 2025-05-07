/***********************************************************************************/
/**
 * NOTE: THE CODE BELOW WILL TRY TO LOCATE PYTHON EXECUTABLE IN "BACKEND" FOLDER TO RUN
 *       SERVER SCRIPTS. SOMETIMES, IT MAY FAIL LOCATING THE CORRECT PYTHON INTERPRETER.
 *       IF THAT'S THE CASE, YOU MAY WANT TO SET PATH TO PYTHON USING THE VARIABLE BELOW.
 */

const PATH_TO_PYTHON = undefined;

/***********************************************************************************/

import fs from 'fs';
import path from 'path';
import { spawn } from 'child_process';

// Move to backend folder
process.chdir('..\\backend');

// Locate python script
let pythonPath = PATH_TO_PYTHON;
if (pythonPath == undefined) {
  let pythonFileName = 'python';

  // Check default venv path
  if (process.platform == 'win32') {
    pythonFileName = 'python.exe';

    if (fs.existsSync('venv\\Scripts\\' + pythonFileName))
      pythonPath = 'venv\\Scripts\\' + pythonFileName;
  } else {
    if (fs.existsSync('venv/bin/' + pythonFileName)) pythonPath = 'venv/bin/' + pythonFileName;
  }

  // If not found yet, search in current folder
  if (pythonPath == undefined)
    fs.readdirSync('.', { recursive: true }).some((file) => {
      if (path.basename(file) == 'python.exe') pythonPath = file;
      return pythonPath != undefined;
    });

  // Finally, set default python interpreter
  if (pythonPath == undefined) pythonPath = 'python3';
}

// Start server
const child = spawn(pythonPath, ['src/main.py']);

// Connect stdout and stderr to console
child.stdout.on('data', (chunk) => console.log(`${chunk}`));
child.stderr.on('data', (chunk) => console.error(`${chunk}`));

// Handle server process exit
child.on('close', (code) => {
  console.log(`Server process exited with code ${code}`);
});
