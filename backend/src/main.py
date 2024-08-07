"""
Start ASGI server to serve FastAPI application.
"""

from multiprocessing import freeze_support
from uvicorn import run as uvicorn_run
from uvicorn.config import LOGGING_CONFIG

from config import CONFIG


if __name__ == '__main__':
    freeze_support()

    api_port = int(CONFIG['APP_API_PORT'])
    uvicorn_run(r"api.app:app", host="0.0.0.0", port=api_port, reload=False, workers=1,
                log_config=LOGGING_CONFIG if not CONFIG['IS_BUNDLED'] else None)
