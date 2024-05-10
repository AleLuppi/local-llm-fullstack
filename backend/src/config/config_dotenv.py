from dotenv import dotenv_values
from os import path

from .bundle_info import is_bundled


if is_bundled:
    raise NotImplementedError("Missing config path for bundled version")
else:
    assert path.basename(path.abspath(path.curdir)) == 'backend', "Application must be run from \"backend\" directory"
    dotenv_path = path.join(path.pardir, "config.env")

config = dotenv_values(dotenv_path)
