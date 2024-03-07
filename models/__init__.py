#!/usr/bin/python3
"""Create a file storage instance and reload the json data."""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
