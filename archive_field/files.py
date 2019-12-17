# -*- coding: utf-8 -*-
import shutil
import tempfile

import os
from archive import Archive
from django.core.files import File
from django.db.models.fields.files import FieldFile

from archive_field.storage import unpack_default_storage


class ArchiveFieldFile(FieldFile):
    def __init__(self, *args, **kwargs):
        super(ArchiveFieldFile, self).__init__(*args, **kwargs)
        self.unpack_storage = getattr(self.field, 'unpack_storage', None) or unpack_default_storage

    def _generate_unpack_folder(self, name):
        return os.path.splitext(name)[0]

    def _unpacked_name(self):
        if self.name:
            return self._generate_unpack_folder(self.name)

    unpacked_name = property(_unpacked_name)

    def _unpacked_path(self):
        if self.name:
            return self.unpack_storage.path(self.unpacked_name)

    unpacked_path = property(_unpacked_path)

    def _unpacked_url(self):
        if self.name:
            return self.unpack_storage.url(self.unpacked_name)

    unpacked_url = property(_unpacked_url)

    def unpack_archive(self, replace=True):
        name = self.name

        tmp_file = tempfile.NamedTemporaryFile(suffix=os.path.splitext(name)[-1])
        archive_file = self.file
        self.open()
        shutil.copyfileobj(archive_file, tmp_file.file)
        tmp_file.file.flush()
        archive = Archive(tmp_file.name)
        temp_dir = tempfile.mkdtemp()
        archive.extract(temp_dir)

        unpack_folder = self._generate_unpack_folder(name)
        try:
            for dir, dirs, files in os.walk(temp_dir):
                for _filename in files:
                    abs_path = os.path.join(dir, _filename)
                    storage_path = os.path.join(unpack_folder, os.path.relpath(abs_path, temp_dir))
                    is_exists = self.unpack_storage.exists(storage_path)
                    if is_exists:
                        if not replace:
                            continue
                        else:
                            self.unpack_storage.delete(storage_path)

                    with open(abs_path, 'rb') as f:

                        self.unpack_storage.save(storage_path, File(f))
        finally:
            shutil.rmtree(temp_dir)

    def delete(self, save=True):
        unpacked_path = self.unpacked_path
        super(ArchiveFieldFile, self).delete(save)
        shutil.rmtree(unpacked_path)

    def save(self, name, content, save=True):
        is_commited = self._committed
        super(ArchiveFieldFile, self).save(name, content, save)
        if not is_commited:
            self.unpack_archive()
