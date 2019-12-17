# -*- coding: utf-8 -*-
from django.conf import settings

# TODO Settings wrapper

DEFAULT_FILE_STORAGE = getattr(settings, 'ARCHIVE_FIELD_UNPACKED_FILE_STORAGE',
                               'django.core.files.storage.FileSystemStorage')
