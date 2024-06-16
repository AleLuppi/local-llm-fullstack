import sys
from os import path


# Check if running in a PyInstaller bundle
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    is_bundled = True
else:
    is_bundled = False

# Get local app path
if is_bundled:
    app_path = sys._MEIPASS
else:
    app_path = path.abspath(path.join(path.curdir, 'src'))
