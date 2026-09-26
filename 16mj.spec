# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path
root = Path(SPECPATH)
a = Analysis([str(root / 'p16mj.py')], pathex=[str(root)],
             binaries=[], datas=[(str(root / 'Image'), 'Image'),
                                 (str(root / 'wqy-zenhei.ttf'), '.')],
             hiddenimports=[], hookspath=[], runtime_hooks=[], excludes=[])
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, a.binaries, a.datas, [], name='16mj',
          debug=False, strip=False, upx=True, console=False)
