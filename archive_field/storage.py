# -*- coding: utf-8 -*-
from django.core.files.storage import get_storage_class
from django.utils.functional import LazyObject

from .settings import DEFAULT_FILE_STORAGE


class UnpackDefaultStorage(LazyObject):
    def _setup(self):
        self._wrapped = get_storage_class(
            DEFAULT_FILE_STORAGE)()


unpack_default_storage = UnpackDefaultStorage()