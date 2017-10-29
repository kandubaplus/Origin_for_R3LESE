# -*- mode: python -*-

block_cipher = None


a = Analysis(['Origib_for_R3LESE.py'],
             pathex=['c:\\Users\\host\\source\\repos\\Origin_for_R3LESE\\Origin_for_R3LESE'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Origib_for_R3LESE',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='icon.ico')
