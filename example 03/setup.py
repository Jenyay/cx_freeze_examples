# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('example_03.py')]

excludes = ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib',
            'xml', 'bz2']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
    }
}

setup(name='hello_world',
      version='0.0.3',
      description='My Hello World App!',
      executables=executables,
      options=options)
