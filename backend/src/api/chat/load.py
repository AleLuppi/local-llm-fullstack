"""
File: load.py

API methods to load chat messages from local storage.
"""
from database.read import read_chats, read_chat
from models import Chat


def load_history(limit: int = None):
    """
    Retrieve all chat messages.

    :param limit: maximum number of messages to retrieve.
    :return: list of all chat messages.
    """
    # Get and sort chats by last update
    chats = read_chats()
    chats = sorted(chats, key=lambda x: x.last_update, reverse=True)

    # Retrieve limited number of recent chats
    if limit is not None:
        chats = chats[:limit]

    return chats


def load_chat(chat_id: str):
    """
    Retrieve chat messages by ID.

    :param chat_id: ID of the chat to retrieve
    :return: chat messages associated to selected ID, or None if not found.
    """
    return read_chat(chat_id)


def resolve_chat(chat_id: str | None = None, create_if_missing: bool = False) -> Chat | None:
    """
    Retrieve chat by ID, or create a new one if ID is not provided.

    NOTE: Output can be None if chat_id is provided but no chat can be found
          with specified ID. To avoid this, set create_if_missing to True.

    :param chat_id: ID of the chat to retrieve
    :param create_if_missing: flag to create a new chat if not found.
    :return: chat messages associated to selected ID, or None if not found.
    """
    # Load or build the chat as required
    if chat_id is not None:
        chat = load_chat(chat_id)
        if chat is None and create_if_missing:
            chat = Chat([], uid=chat_id)
    else:
        chat = Chat([])

    return chat
