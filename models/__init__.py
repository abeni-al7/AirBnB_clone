#!/usr/bin/python3
"""An initializer module"""

import models.engine.file_storage

storage = models.engine.file_storage.FileStorage()
storage.reload()
