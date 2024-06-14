from langchain_core.messages import ChatMessage


system_message_label = "<SYSTEM>"
human_message_label = "<HUMAN>"
ai_message_label = "<AI>"


class __FixedRoleChatMessage(ChatMessage):
    def __init__(self, **kwargs):
        kwargs.pop("role", None)
        super().__init__(**kwargs)


class SystemMessage(__FixedRoleChatMessage):
    role = system_message_label


class HumanMessage(__FixedRoleChatMessage):
    role = human_message_label


class AIMessage(__FixedRoleChatMessage):
    role = ai_message_label
