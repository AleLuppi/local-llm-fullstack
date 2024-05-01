"""
File: router.py

Set API routes for chat management.
"""

from fastapi import APIRouter, status

from .load import load_history, load_chat

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
