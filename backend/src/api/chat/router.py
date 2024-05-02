"""
File: router.py

Set API routes for chat management.
"""

from fastapi import APIRouter, status

from .load import load_history, load_chat
from .save import save_user_message

# Init router
router = APIRouter()


@router.get("/history", status_code=status.HTTP_200_OK)
def get_chats(limit: int = None):
    """
    Retrieve all chat messages.

    :param limit: maximum number of messages to retrieve.
    :return: list of all chat messages.
    """
    return load_history(limit=limit)


@router.get("/{chat_id}", status_code=status.HTTP_200_OK)
def get_chat(chat_id: str):
    """
    Retrieve chat messages by ID.

    :param chat_id: ID of the chat to retrieve
    :return: list of chat messages associated to selected chat ID.
    """
    return load_chat(chat_id)


@router.put("/new", status_code=status.HTTP_200_OK)
def create_chat(message: str | None = None):
    """
    Append a message to the selected chat.

    :param message: optional chat message to start the chat with.
    :return: chat associated to selected chat ID.
    """
    # Save chat message into a new chat
    # NOTE: chat messages stored via API will be saved with USER role
    chat = save_user_message(None, message)
    return chat.to_dict() if chat is not None else None

