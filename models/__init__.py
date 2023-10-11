#!/usr/bin/python3
"""
Package Initialization file to set up Storage System in the program
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
