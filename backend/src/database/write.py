from tinydb.table import Document
from typing import TYPE_CHECKING

from .__db import db_chat
from models.chat_models import ChatMessage
from .read import read_chat

if TYPE_CHECKING:
    from models import Chat, ChatRole


def write_chat(chat: 'Chat'):
    """
    Insert a new chat object into the database.

    :param chat: chat object to store.
    :return: document ID, or None if insertion failed.
    """
    try:
        return db_chat.insert(Document(chat.to_dict(), doc_id=chat.id))
    except ValueError:
        # Document ID already exists in DB
        return None


def update_chat(chat: 'Chat'):
    """
    Update an existing chat object in the database.

    :param chat: chat object to store.
    :return: updated document ID.
    """
    ids = db_chat.update(chat.to_dict(), doc_ids=[chat.id])
    return ids[0] if len(ids) > 0 else None


def append_to_chat(chat: 'Chat', message: str, role: 'ChatRole'):
    """
    Append a message to the selected chat.

    :param chat: chat object to store.
    :param message: chat message to store.
    :param role: agent role for the message.
    :return: document ID.
    """
    chat.add_message(ChatMessage(role, message))
    if read_chat(chat.id):
        return update_chat(chat)
    else:
        return write_chat(chat)
