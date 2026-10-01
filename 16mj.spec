# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path
import sys

# PyInstaller can finish with missing-import warnings. Fail before creating an
# unusable executable if the build interpreter cannot load the game's library.
try:
    import pygame
    import pygame.display
    import pygame.image
    import pygame.font
except ImportError as exc:
    raise SystemExit(
        f'Cannot load pygame in the build environment: {exc}\n'
        f'Install build dependencies with:\n'
        f'  "{sys.executable}" -m pip install -r "{Path(SPECPATH) / "requirements-build.txt"}"\n'
        f'Then run PyInstaller with the same Python interpreter.'
    ) from exc

root = Path(SPECPATH)
a = Analysis([str(root / 'p16mj.py')], pathex=[str(root)],
             binaries=[], datas=[(str(root / 'Image'), 'Image'),
                                 (str(root / 'wqy-zenhei.ttf'), '.')],
             hiddenimports=[], hookspath=[], runtime_hooks=[], excludes=[])
pyz = PYZ(a.pure)
# Including binaries and data directly in EXE creates a one-file executable.
# PyInstaller's pygame hook collects its native SDL dependencies.
exe = EXE(pyz, a.scripts, a.binaries, a.datas, [], name='16mj',
          debug=False, strip=False, upx=True, console=False)
