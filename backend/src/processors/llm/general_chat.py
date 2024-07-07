from os.path import basename
from langchain_core.messages import BaseMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from assets import LLM_MODEL_MISTRAL_7B
from models import Chat, ChatRole
from .__prompts import prompt_common_qa, prompt_common_qa_summary
from .__messages import SystemMessage, HumanMessage, AIMessage
from .__processor_llm import ProcessorLLM


# Init model
llm = ProcessorLLM(path=LLM_MODEL_MISTRAL_7B, prompt=prompt_common_qa,
                   download=rf"https://gpt4all.io/models/gguf/{basename(LLM_MODEL_MISTRAL_7B)}")


def __chat_to_messages(chat: Chat) -> [BaseMessage]:
    """
    Translate chat into messages to pass to LLM.

    :param chat: chat to translate.
    :return: messages to pass to LLM.
    """
    return [
        (HumanMessage if message.role == ChatRole.USER else
         AIMessage if message.role == ChatRole.AGENT else
         SystemMessage)(content=message.content) for message in chat.messages
        if message.role in [ChatRole.USER, ChatRole.AGENT, ChatRole.SYSTEM]
    ]


def query_llm(query: str) -> str:
    """
    Query LLM as User with a single message.

    :param query: query to pass to LLM.
    :return: LLM response.
    """
    return llm.invoke([
        HumanMessage(content=query),
    ])


def chat_llm(chat: Chat | str) -> str:
    """
    Chat with LLM with multiple messages.

    :param chat: messages to pass to LLM.
    :return: LLM response.
    """
    # Single query case
    if isinstance(chat, str):
        return query_llm(chat)

    # Translate chat into messages to pass to LLM
    messages = __chat_to_messages(chat)

    # Chat history case
    return llm.invoke(messages)


def summarize_chat(chat: Chat | str) -> str:
    """
    Summarize chat with LLM.

    :param chat: chat to summarize.
    :return: summarized chat.
    """
    # Init prompt
    summary_prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content=prompt_common_qa_summary),
        MessagesPlaceholder(variable_name="messages"),
        SystemMessage(content="Short summary of the chat: "),
    ])

    # Get summary llm
    summary_llm = llm.clone()
    summary_llm.prompt = summary_prompt

    return summary_llm.invoke(__chat_to_messages(chat)).strip('."').capitalize()

