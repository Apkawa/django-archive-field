# -*- coding: utf-8 -*-

from django.db.models import FileField

from archive_field import files

__all__ = ['ArchiveFileField']


class ArchiveFileField(FileField):
    attr_class = files.ArchiveFieldFile

    def __init__(self, *args, **kwargs):
        super(ArchiveFileField, self).__init__(*args, **kwargs)
        self.unpack_storage = kwargs.get('unpack_storage')
