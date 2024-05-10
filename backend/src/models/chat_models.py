from datetime import datetime as datetime_cls
from typing import TYPE_CHECKING
from uuid import uuid4

if TYPE_CHECKING:
    from .role_models import ChatRole


class ChatMessage:
    def __init__(self, role: 'ChatRole', content: str, datetime: datetime_cls | str = None):
        self._role = role
        self._content = content
        self.datetime = datetime if datetime is not None else datetime_cls.now()

    @property
    def role(self):
        return self._role

    @property
    def content(self):
        return self._content

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, value: datetime_cls | str):
        self._datetime = datetime_cls.fromisoformat(value) if isinstance(value, str) else value

    def to_dict(self):
        return {
            "role": self._role,
            "content": self._content,
            "datetime": self._datetime.isoformat(),
        }


class Chat:
    def __init__(self, messages: list['ChatMessage'], uid: str | int = None, summary: str = None,
                 creation_datetime: datetime_cls | str = None):
        self._id = int(uid) if uid is not None else uuid4().int
        self._messages = messages
        self._summary = summary
        self.creation_datetime = creation_datetime if creation_datetime is not None else datetime_cls.now()


    @property
    def id(self):
        return self._id

    @property
    def messages(self):
        return sorted(self._messages, key=lambda x: x.datetime)

    @property
    def summary(self):
        return self._summary

    @property
    def creation_datetime(self):
        return self._creation_datetime

    @creation_datetime.setter
    def creation_datetime(self, value: datetime_cls | str):
        self._creation_datetime = datetime_cls.fromisoformat(value) if isinstance(value, str) else value

    @property
    def last_message(self):
        return self.messages[-1] if len(self.messages) > 0 else None

    @property
    def last_update(self):
        return self.last_message.datetime if self.last_message is not None else self.creation_datetime

    def add_message(self, message: 'ChatMessage'):
        self._messages.append(message)

    def to_dict(self):
        return {
            "id": str(self._id),
            "messages": [message.to_dict() for message in self._messages],
            "summary": self._summary,
            "creation_datetime": self._creation_datetime.isoformat(),
        }

    @classmethod
    def from_dict(cls, param):
        return cls([ChatMessage(**message) for message in param["messages"]], uid=param["id"],
                   summary=param["summary"], creation_datetime=param["creation_datetime"])
