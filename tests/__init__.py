#!/usr/bin/python3
"""Tests module"""
import os
from typing import TextIO
from models.engine.file_storage import FileStorage


def clear_stream(stream: TextIO):
    """Clears the contents of a given stream"""
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)
