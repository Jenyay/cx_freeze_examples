# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('example.py')]

excludes = ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib',
            'xml', 'pydoc', 'doctest', 'argparse', 'datetime', 'zipfile',
            'subprocess', 'pickle', 'threading', 'locale', 'calendar', 'functools',
            'weakref', 'tokenize', 'base64', 'gettext', 'heapq', 're', 'operator',
            'bz2', 'fnmatch', 'getopt', 'reprlib', 'string', 'stringprep',
            'contextlib', 'quopri', 'copy', 'imp', 'keyword', 'linecache']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
    }
}

setup(name='hello_world',
      version='0.0.4',
      description='My Hello World App!',
      executables=executables,
      options=options)
