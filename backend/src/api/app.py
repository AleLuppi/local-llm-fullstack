"""
Entry point to invoke FastAPI application service.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.utils import router as router_utils
from api.chat import router as router_chat
from config import config

# Init app
app = FastAPI()

# Setup origins
origins = [
    f"http://localhost:{config['APP_API_PORT']}",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:9000",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup routers
app.include_router(router_utils)
app.include_router(router_chat, prefix="/chat")
