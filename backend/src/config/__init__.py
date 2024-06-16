from os import path
from .bundle_info import is_bundled, app_path

if not is_bundled:
    assert path.basename(path.abspath(path.curdir)) == 'backend', "Application must be run from \"backend\" directory"

from .config_dotenv import config as dotenv_config


CONFIG = {
    'IS_BUNDLED': is_bundled,
    'APP_PATH': app_path,
    **dotenv_config,
}
