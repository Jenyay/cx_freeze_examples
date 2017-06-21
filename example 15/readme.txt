В пути до setup.py не должно быть русских букв, иначе будет возникать ошибка:

Traceback (most recent call last):
  File "setup.py", line 27, in <module>
    options=options)
  File "C:\Users\jenyay\AppData\Roaming\Python\Python36\site-packages\cx_Freeze\dist.py", line 349, in setup
    distutils.core.setup(**attrs)
  File "C:\Program Files (x86)\Python36-32\lib\distutils\core.py", line 148, in setup
    dist.run_commands()
  File "C:\Program Files (x86)\Python36-32\lib\distutils\dist.py", line 955, in run_commands
    self.run_command(cmd)
  File "C:\Program Files (x86)\Python36-32\lib\distutils\dist.py", line 974, in run_command
    cmd_obj.run()
  File "C:\Users\jenyay\AppData\Roaming\Python\Python36\site-packages\cx_Freeze\windist.py", line 392, in run
    self.add_files()
  File "C:\Users\jenyay\AppData\Roaming\Python\Python36\site-packages\cx_Freeze\windist.py", line 133, in add_files
    cab.commit(db)
  File "C:\Program Files (x86)\Python36-32\lib\msilib\__init__.py", line 217, in commit
    FCICreate(filename, self.files)
ValueError: FCI error 1


Из setup.py убран параметр, указывающий папку для сборки.
