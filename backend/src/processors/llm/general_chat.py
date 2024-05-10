from langchain_community.llms import GPT4All
from langchain_core.messages import BaseMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from assets import LLM_MODEL_MISTRAL_7B
from models import Chat, ChatRole
from .__prompts import prompt_common_qa
from .__messages import SystemMessage, HumanMessage, AIMessage


# Init model
llm_model = GPT4All(model=LLM_MODEL_MISTRAL_7B)

# Init prompt
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content=prompt_common_qa),
    MessagesPlaceholder(variable_name="messages"),
    AIMessage(content=""),
])

# Create chain
llm_chain = prompt | llm_model


def __invoke_llm(messages: [BaseMessage]) -> str:
    """
    Invoke LLM with messages.

    :param messages: messages to pass to LLM.
    :return: LLM response.
    """
    return str(llm_chain.invoke({"messages": messages})).strip()


def query_llm(query: str) -> str:
    """
    Query LLM as User with a single message.

    :param query: query to pass to LLM.
    :return: LLM response.
    """
    return __invoke_llm([
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
    messages = [
        (HumanMessage if message.role == ChatRole.USER else
         AIMessage if message.role == ChatRole.AGENT else
         SystemMessage)(content=message.content) for message in chat.messages
        if message.role in [ChatRole.USER, ChatRole.AGENT, ChatRole.SYSTEM]
    ]

    # Chat history case
    return __invoke_llm(messages)
