# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('hello_01.py', targetName='hello_world_01.exe'),
               Executable('hello_02.py', targetName='hello_world_02.exe'),
               ]

excludes = ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib',
            'xml', 'pydoc', 'doctest', 'argparse', 'datetime', 'zipfile',
            'subprocess', 'pickle', 'threading', 'locale', 'calendar',
            'tokenize', 'base64', 'gettext',
            'bz2', 'fnmatch', 'getopt', 'string', 'stringprep',
            'contextlib', 'quopri', 'copy', 'imp', 'linecache']

zip_include_packages = ['collections', 'encodings', 'importlib', 'json']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
    }
}

setup(name='hello_world',
      version='0.0.9',
      description='My Hello World App!',
      executables=executables,
      options=options)
