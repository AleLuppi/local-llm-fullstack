from .bundle_info import is_bundled
from .config_dotenv import config as dotenv_config


config = {
    'IS_BUNDLED': is_bundled,
    **dotenv_config,
}
