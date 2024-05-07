from enum import Enum


class ChatRole(str, Enum):
    USER = "user"
    AGENT = "agent"
    SYSTEM = "system"
    FUNCTION = "function"
