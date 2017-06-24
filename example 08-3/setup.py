# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('example.py', targetName='hello_world.exe')]

excludes = ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib',
            'xml', 'pydoc', 'doctest', 'argparse', 'datetime', 'zipfile',
            'subprocess', 'pickle', 'threading', 'locale', 'calendar',
            'tokenize', 'base64', 'gettext',
            'bz2', 'fnmatch', 'getopt', 'string', 'stringprep',
            'contextlib', 'quopri', 'copy', 'imp', 'linecache']

includes = ['json']

zip_include_packages = ['collections', 'encodings', 'importlib', 'json']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
    }
}

setup(name='hello_world',
      version='0.0.8',
      description='My Hello World App!',
      executables=executables,
      options=options)
