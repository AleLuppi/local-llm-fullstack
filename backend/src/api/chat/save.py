"""
File: save.py

API methods to locally store chat messages.
"""
from database.write import write_chat, append_to_chat, update_chat
from models import ChatRole, Chat
from .load import resolve_chat


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
    :param message: user chat message to store.
    :return: updated chat with user message.
    """
    # Append message to chat
    append_to_chat(chat, message, ChatRole.USER)
    return chat


def save_agent_message(chat: Chat, message: str) -> Chat:
    """
    Append an agent message to the selected chat.

    :param chat: chat to append message to.
    :param message: agent chat message to store.
    :return: updated chat with user message.
    """
    # Append message to chat
    append_to_chat(chat, message, ChatRole.AGENT)
    return chat


def save_chat_summary(chat: Chat, summary: str, *, force: bool = True) -> Chat:
    """
    Save chat summary.

    :param chat: chat to save summary of.
    :param summary: chat summary to save.
    :param force: flag to force chat update, even if summary is unchanged.
    :return: updated chat with summary.
    """
    # Save summary
    prev_summary = chat.summary
    chat.summary = summary
    if prev_summary != summary or force:
        update_chat(chat)

    return chat
