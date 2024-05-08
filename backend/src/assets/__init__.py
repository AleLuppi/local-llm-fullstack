from os.path import abspath, join as path_join, dirname


def resolve(*paths: str):
    """
    Resolve a path relative to the "assets" directory.

    :param paths: path components to join.
    :return: absolute path resolved to the "assets" directory.
    """
    # Base "assets" directory name
    __DIR_NAME = dirname(__file__)

    return abspath(path_join(__DIR_NAME, *paths))


LLM_MODEL_MISTRAL_7B = resolve("models", "mistral-7b-openorca.gguf2.Q4_0.gguf")
