from setuptools import setup

APP = ['NASCAR/app.py']
DATA_FILES = [('NASCAR', ['NASCAR/getinfo.py', 'NASCAR/sql_client.py'])]  # Define data files within the 'NASCAR' subdirectory.

OPTIONS = {
    'argv_emulation': True,
    'packages': [],  # Remove 'sys' and 'os'; they are part of the standard library and do not need to be included.
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
