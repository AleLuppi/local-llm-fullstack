from asyncio import ensure_future
from pathlib import Path
from urllib import request
from urllib.error import HTTPError, URLError
from typing import TypedDict, NotRequired, Optional

from langchain_core.language_models import BaseLLM
from langchain_core.messages import BaseMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.llms import GPT4All

from config import CONFIG
from .__messages import SystemMessage, HumanMessage, AIMessage


class ModelInfo(TypedDict):
    name: str
    path: str
    model: Optional[BaseLLM]
    download_url: NotRequired[Optional[str]]
    download_progress: NotRequired[float]


class ProcessorLLM:
    """
    Base class for LLM processors.
    """

    # Store all models already initialized
    _models: dict[str, ModelInfo] = {}


    def __init__(self, path: str | Path = None, prompt: str | ChatPromptTemplate = None, download: str = None):
        """
        Init LLM model.

        :param path: path to model.
        :param prompt: system prompt to set up template, or prompt template.
        :param download: url to download model from.
        """
        super().__init__()

        self._model: ModelInfo | None = None
        self.prompt = prompt

        if path is not None:
            self.set_model(path, download)

    @property
    def model(self) -> ModelInfo | None:
        """
        Get LLM model info.

        :return: LLM model info.
        """
        return self._model

    @property
    def prompt(self) -> ChatPromptTemplate | None:
        """
        Get model prompt.

        :return: model prompt.
        """
        return self._prompt

    @prompt.setter
    def prompt(self, value: str | ChatPromptTemplate):
        """
        Set model prompt.

        :param value: system prompt to update model prompt.
        """
        if isinstance(value, str):
            self._prompt = ChatPromptTemplate.from_messages([
                SystemMessage(content=value),
                MessagesPlaceholder(variable_name="messages"),
                AIMessage(content=""),
            ])
        else:
            self._prompt = value

    def set_model(self, path: str | Path, download: str = None):
        """
        Set LLM model to use.

        :param path: path to model.
        :param download: url to download model from.
        """
        model_path = Path(path).absolute()
        self._model: ModelInfo = {
            "name": model_path.stem.lower(),
            "path": str(model_path),
            "model": None,
            "download_url": download,
            "download_progress": 0,
        }
        self._init_model()

    def _init_model(self):
        """
        Retrieve or initialize model.
        """
        # Retrieve current model
        stored_model = self._models.get(self.model["name"])
        if stored_model is not None:
            stored_model.update({k: v for k, v in self.model.items() if v is not None})
            self._model = stored_model
        else:
            self._models[self.model['name']] = self.model

        # Initialize model if not already done
        if self.model['model'] is None:
            ensure_future(self._prepare_model())

    async def _prepare_model(self):
        """
        Ensure LLM model is ready to use.

        Either initialize model or download if missing.
        """
        if Path(self.model["path"]).exists():
            self.model['model'] = GPT4All(model=self.model["path"])
            self._models[self.model["name"]] = self.model
        elif self.model.get('download_url'):
            await self._download_model()
            await self._prepare_model()

    async def _download_model(self, model_info: ModelInfo = None):
        """
        Download LLM model from url.

        :param model_info: optional model info with download url.
        """
        # Start download of model
        if model_info is None:
            model_info = self.model
        model_name = model_info["name"]
        model_url = model_info["download_url"]
        try:
            if model_url is None:
                raise URLError(f"Model {model_name} has no download url.")
            opener = request.build_opener()
            opener.addheaders = [('User-Agent', f'{CONFIG["APP_API_NAME"]}/{CONFIG["APP_API_VERSION"]}')]
            request.install_opener(opener)
            request.urlretrieve(model_url, model_info["path"],
                                lambda blocks_num, block_size, total_size, model=model_name:
                                self._download_progress(blocks_num, block_size, total_size, model))

            # Finally, make sure download is set as complete
            self._models[model_name]["download_url"] = model_url
            self._models[model_name]["download_progress"] = 1

        except (URLError, HTTPError):
            # Set download as failed
            self._models[model_name]["download_url"] = model_url
            self._models[model_name]["download_progress"] = 0

    def _download_progress(self, blocks_num, block_size, total_size, model_name: str):
        """
        Update download progress info.

        :param blocks_num: number of blocks downloaded so far.
        :param block_size: size of each block.
        :param total_size: total size of download.
        :param model_name: name of model being downloaded.
        """
        # Store download progress
        self._models[model_name]["download_url"] = (blocks_num * block_size) / total_size

    def invoke(self, messages: [BaseMessage] = ()) -> str:
        """
        Invoke LLM chain with messages.

        :param messages: messages to pass to LLM.
        :return: LLM response.
        """
        llm_chain = self.prompt | self.model['model']
        return str(llm_chain.invoke({"messages": messages})).strip()

    def clone(self):
        """
        Clone LLM.

        :return: cloned LLM processor.
        """
        cloned = self.__class__(path=self.model["path"])
        cloned.prompt = self.prompt
        return cloned
