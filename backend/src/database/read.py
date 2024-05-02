from .__db import db_chat
from models.chat_models import Chat


def read_chats():
    """
    Retrieve all chat messages.

    :return: list of all chat messages.
    """
    return [Chat.from_dict(chat) for chat in db_chat.all()]


def read_chat(chat_id: str):
    """
    Insert a new chat object into the database.

    :param chat_id: ID of the chat to retrieve.
    :return: selected chat, or None if not found.
    """
    chat = db_chat.get(doc_id=chat_id)
    if chat is None:
        return None
    return Chat.from_dict(chat)
