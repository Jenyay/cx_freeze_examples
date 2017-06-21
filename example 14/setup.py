from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('example_14.py', base=base, targetName = 'hello.exe')
]

setup(name='My project',
      version = '0.0.14',
      description = 'Example for article.',
      options = dict(build_exe = buildOptions),
      executables = executables)
