from models import Chat
from .query import chat_agent, chat_summarize_agent
from .save import save_user_message, save_agent_message, save_chat_summary


def handle_user_message(chat: Chat, message: str, reply: bool = False) -> Chat:
    """
    Handle a user message.

    :param chat: reference chat that shall be updated.
    :param message: user chat message to store.
    :param reply: flag to ask for llm answer generation.
    :return: updated chat.
    """
    # NOTE: chat messages stored via API will be saved with USER role
    save_user_message(chat, message)

    # Optionally create and store the agent message
    if reply:
        agent_message = chat_agent(chat)
        save_agent_message(chat, agent_message)

    # Create and store chat summary if required
    chat_summary = create_chat_summary(chat)
    save_chat_summary(chat, chat_summary)

    return chat


def create_chat_summary(chat: Chat) -> str:
    """
    Create and store a chat summary.

    :param chat: reference chat that shall be summarized.
    :return: chat summary.
    """
    # Summarize chat if necessary
    if chat.summary is None:
        summary = chat_summarize_agent(chat)
    else:
        summary = chat.summary

    return summary
