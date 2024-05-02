"""
File: save.py

API methods to locally store chat messages.
"""
from database.read import read_chat
from database.write import write_chat, append_to_chat
from models import ChatRole, Chat


def save_user_message(chat_id: str | None, message: str | None):
    """
    Append a user message to the selected chat.

    :param chat_id: ID of the chat to append to.
    :param message: chat message to store.
    :return: chat associated to selected chat ID.
    """
    # Create new chat if needed
    if chat_id is None:
        chat = Chat([])
    # Else retrieve existing chat
    else:
        chat = read_chat(chat_id)

    # Append message to chat
    if chat is not None:
        if message is None:
            write_chat(chat)
        else:
            append_to_chat(chat, message, ChatRole.USER)
    return chat
