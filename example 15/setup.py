# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('example_15.py',
                          targetName='hello_wx.exe',
                          base='Win32GUI',
                          icon='example.ico')]

excludes = ['logging', 'unittest', 'email', 'html', 'http', 'urllib', 'xml',
            'unicodedata', 'bz2', 'select']

zip_include_packages = ['collections', 'encodings', 'importlib', 'wx']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'zip_include_packages': zip_include_packages,
    }
}

setup(name='hello_world',
      version='0.0.15',
      description='My Hello World App!',
      executables=executables,
      options=options)
