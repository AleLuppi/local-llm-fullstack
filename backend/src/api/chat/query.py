"""
File: query.py

API methods to provide answers to queries in chat.
"""

from processors.llm.general_chat import query_llm, chat_llm
from models import Chat


def query_agent(query: Chat | str) -> str:
    """
    Query LLM to answer a single message.

    :param query: query, or current chat, to pass to LLM.
    :return: LLM response.
    """
    if isinstance(query, Chat):
        if query.last_message is None:
            return query_llm("")
        return query_llm(query.last_message.content)
    return query_llm(query)


def chat_agent(chat: Chat) -> str:
    """
    Chat with LLM with multiple messages.

    :param chat: messages to pass to LLM.
    :return: LLM response.
    """
    return chat_llm(chat)
