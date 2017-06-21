# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('example_01.py')]

setup(name='hello_world',
      version='0.0.1',
      description='My Hello World App!',
      executables=executables)
