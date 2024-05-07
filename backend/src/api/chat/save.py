"""
File: save.py

API methods to locally store chat messages.
"""
from database.write import write_chat, append_to_chat
from models import ChatRole, Chat
from .load import resolve_chat
from .query import chat_agent


def save_new_chat(chat: Chat | None = None) -> Chat:
    """
    Save a new chat.

    :param chat: optional chat to save, a new one will be created if not provided.
    :return: updated chat.
    """
    if chat is None:
        chat = resolve_chat()
    write_chat(chat)
    return chat


def save_user_message(chat: Chat, message: str) -> Chat:
    """
    Append a user message to the selected chat.

    :param chat: chat to append message to.
    :param message: chat message to store.
    :return: updated chat with user message.
    """
    # Append message to chat
    append_to_chat(chat, message, ChatRole.USER)
    return chat


def save_agent_message(chat: Chat, message: str | None = None) -> Chat:
    """
    Append an agent message to the selected chat.

    :param chat: chat to append message to.
    :param message: optional chat message to store, otherwise a new answer will be generated.
    :return: updated chat with user message.
    """
    # Optionally create the agent message
    if message is None:
        message = chat_agent(chat)

    # Append message to chat
    append_to_chat(chat, message, ChatRole.AGENT)
    return chat