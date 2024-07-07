from dotenv import dotenv_values
from os import path

from .bundle_info import is_bundled, app_path


if is_bundled:
    dotenv_path = path.join(app_path, "config", "config.env")
else:
    dotenv_path = path.join(path.pardir, "config.env")

config = dotenv_values(dotenv_path)
