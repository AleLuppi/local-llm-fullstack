from os import path

from config import CONFIG


def resolve(*paths: str):
    """
    Resolve a path relative to the "assets" directory.

    :param paths: path components to join.
    :return: absolute path resolved to the "assets" directory.
    """
    # Join paths to base "assets" directory name
    return path.abspath(path.join(
        CONFIG['APP_PATH'],
        path.basename(path.dirname(__file__)),
        *paths
    ))


LLM_MODEL_MISTRAL_7B = resolve("models", "mistral-7b-openorca.gguf2.Q4_0.gguf")
