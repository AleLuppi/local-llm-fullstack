from dotenv import dotenv_values

from .bundle_info import is_bundled


if is_bundled:
    raise NotImplementedError("Missing config path for bundled version")
else:
    dotenv_path = "../../config.env"

config = dotenv_values(dotenv_path)
