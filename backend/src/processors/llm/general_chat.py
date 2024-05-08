from langchain_community.llms import GPT4All
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from assets import LLM_MODEL_MISTRAL_7B
from models import Chat, ChatRole


# Init model
llm_model = GPT4All(model=LLM_MODEL_MISTRAL_7B)

# Init prompt
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant."),
    MessagesPlaceholder(variable_name="messages"),
])

# Create chain
llm_chain = prompt | llm_model


def query_llm(query: str) -> str:
    """
    Query LLM as User with a single message.

    :param query: query to pass to LLM.
    :return: LLM response.
    """
    return llm_chain.invoke({"messages": [
        HumanMessage(content=query),
    ]})


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
    return llm_chain.invoke({"messages": messages})
