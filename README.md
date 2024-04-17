# Python + Vue.js for a local LLM QA

Build and chat with a local (private) LLM. Or just use this as a starting point to integrate Vue.js with Python in your own _cool_ application 👾

## SW stack

### Frontend

- [**Vue.js 3**](https://vuejs.org/) as frontend dev framework.
  - using Composition API with _script setup_
  - with [**TypeScript**](https://www.typescriptlang.org/) as scripting language
- [**Quasar**](https://quasar.dev/) as UI library and to bundle frontend package.
  - with [**Vite**](https://vitejs.dev/) as dev server and bundler
- [**Electron**](https://www.electron.build/) to build distributable desktop app.
- [**Vitest**](https://vitest.dev/) for unit and integration tests.

### Backend

- [**Python**](https://www.python.org/) as programming language.
- [**LangChain**](https://www.langchain.com/) to ease LLM querying.
- [**FastAPI**](https://fastapi.tiangolo.com/) to prepare a simple REST API.
  - with [**Uvicorn**](https://www.uvicorn.org/) as ASGI web server
- [**PyInstaller**](https://pyinstaller.org/) to bundle Python application.
