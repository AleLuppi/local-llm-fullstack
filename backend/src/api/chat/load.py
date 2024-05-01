"""
File: load.py

API methods to load chat messages from local storage.
"""
from database.read import read_chats, read_chat


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
