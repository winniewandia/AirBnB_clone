#!/usr/bin/python3
"""This module creates an instance of FileStorage
It imports the models engine filestorage
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

