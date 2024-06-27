# -*- mode: python ; coding: utf-8 -*-
import os
import sys
import gpt4all
sys.path.append(os.getcwd())

# Get app config
from src.config import CONFIG


a = Analysis(
    [r'src\main.py'],
    pathex=[],
    binaries=[
        (os.path.join(os.path.dirname(gpt4all.__file__), 'llmodel_DO_NOT_MODIFY'), 'gpt4all/llmodel_DO_NOT_MODIFY'),
    ],
    datas=[
        ('src/assets', 'assets'),
        ('../config.env', 'config'),
    ],
    hiddenimports=[
        'api.app',
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=CONFIG['APP_API_NAME'],
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=CONFIG['APP_API_NAME'],
)
