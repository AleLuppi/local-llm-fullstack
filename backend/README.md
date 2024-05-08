# [Backend] **_Python_** + Vue.js for a local LLM QA

Backend portion of the application: serve a LLM model query capability via an API, developed in Python.

## Get started

> Tested with **python 3.11**

Get started in minutes by following these steps:

1.  `cd` into `backend` folder, create a virtual environment (_optional, but suggested_), and initialize it via

    ```
    pip install -r requirements.txt
    ```

2.  Download LLM model `mistral-7b-openorca.gguf2.Q4_0.gguf` from [GPT4All](https://gpt4all.io/index.html), and place it under `assets/models`. If you are willing to use a different model, please check [the related section](#config-your-own-model-optional).

3.  Run `main.py` to open your API on `localhost`, e.g.:
    ```
    path/to/venv/python src/main.py
    ```

### Config your own model (_optional_)

Should you use a LLM model different from the base one, you can follow these steps:

1.  Download/move your model under `assets/models`.

2.  Extend `assets/__init__.py` with your own path, e.g.:

    ```python
    LLM_MODEL_MYMODEL = resolve("models", "my_model_file.gguf")
    ```

3.  Update LLM used in `processors/llm/general_chat.py` with your own model:

    ```python
    # If using a different GPT4All model
    from assets import LLM_MODEL_MYMODEL
    llm_model = GPT4All(model=LLM_MODEL_MYMODEL)

    # If using a model not from GPT4All
    from langchain_community.llms import MyProvider # !!! CHOOSE YOUR SOURCE
    from assets import LLM_MODEL_MYMODEL
    llm_model = MyProvider(model=LLM_MODEL_MYMODEL)
    ```
