"""
File: router.py

Set API routes for chat management.
"""

from fastapi import APIRouter, status

from .load import load_history, load_chat, resolve_chat
from .save import save_user_message, save_new_chat, save_agent_message

# Init router
router = APIRouter()


@router.get("/history", status_code=status.HTTP_200_OK)
def get_chats(limit: int = None):
    """
    Retrieve all chat messages.

    :param limit: maximum number of messages to retrieve.
    :return: list of all chat messages.
    """
    return [chat.to_dict() for chat in load_history(limit=limit)]


@router.get("/id/{chat_id}", status_code=status.HTTP_200_OK)
def get_chat(chat_id: str):
    """
    Retrieve chat messages by ID.

    :param chat_id: ID of the chat to retrieve
    :return: list of chat messages associated to selected chat ID.
    """
    chat = load_chat(chat_id)
    return chat.to_dict() if chat is not None else None


@router.post("/id/{chat_id}", status_code=status.HTTP_200_OK)
def append_chat(chat_id: str, message: str, reply: bool = False):
    """
    Append a message to the selected chat.

    :param chat_id: ID of the chat to append to
    :param message: chat message to store.
    :param reply: flag to ask for llm answer generation.
    :return: chat associated to selected chat ID.
    """
    # Retrieve chat
    chat = resolve_chat(chat_id)

    # Save chat message to selected chat
    if chat is not None:
        # NOTE: chat messages stored via API will be saved with USER role
        chat = save_user_message(chat, message)

        if reply:
            chat = save_agent_message(chat)

    return chat.to_dict() if chat is not None else None


@router.post("/new", status_code=status.HTTP_200_OK)
def create_chat(message: str | None = None, reply: bool = False):
    """
    Append a message to the selected chat.

    :param message: optional chat message to start the chat with.
    :param reply: flag to ask for llm answer generation.
    :return: chat associated to selected chat ID.
    """
    # Create a new chat
    chat = save_new_chat()

    # Save chat message into a new chat
    if message is not None:
        # NOTE: chat messages stored via API will be saved with USER role
        chat = save_user_message(chat, message)

        if reply:
            chat = save_agent_message(chat)

    return chat.to_dict() if chat is not None else None
