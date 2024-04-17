"""
Start ASGI server to serve FastAPI application.
"""

from multiprocessing import freeze_support
from uvicorn import run as uvicorn_run

if __name__ == '__main__':
    freeze_support()
    uvicorn_run(r"api.app:app", host="0.0.0.0", port=48314, reload=False, workers=2)
