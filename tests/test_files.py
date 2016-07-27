# coding: utf-8
from __future__ import unicode_literals

import shutil

import os
from unittest import TestCase

from django.conf import settings
from django.core.files.base import ContentFile

from archive_field.fields import ArchiveFileField
from archive_field.files import ArchiveFieldFile


class ArchiveFileFieldTestCase(TestCase):
    def setUp(self):
        self.archive = os.path.join(settings.FIXTURES_ROOT, 'test.zip')
        self.upload_to = 'archive'

    def test_generic(self):
        field = ArchiveFileField(name='test', upload_to=self.upload_to)
        fake_model = type(b'fake', (object,), {field.name: None})
        _file = ArchiveFieldFile(field=field, instance=fake_model(), name='')
        _file._committed = False
        with open(self.archive, 'rb') as f:
            _file.save('test.zip', ContentFile(f.read()), save=False)

        self.assertEqual(_file.unpacked_path, os.path.join(settings.MEDIA_ROOT, os.path.splitext(_file.name)[0]))
        self.assertEqual(_file.unpacked_url, os.path.join(settings.MEDIA_URL, os.path.splitext(_file.name)[0]))
        self.assertTrue(os.path.exists(_file.unpacked_path))

        # Cleanup
        shutil.rmtree(os.path.dirname(_file.path))

    def test_delete(self):
        field = ArchiveFileField(name='test', upload_to='test/example_360/')
        fake_model = type(b'fake', (object,), {field.name: None})
        _file = ArchiveFieldFile(field=field, instance=fake_model(), name='')
        _file._committed = False
        with open(self.archive, 'rb') as f:
            _file.save('test.zip', ContentFile(f.read()), save=False)

        self.assertEqual(_file.unpacked_path, os.path.join(settings.MEDIA_ROOT, os.path.splitext(_file.name)[0]))
        self.assertEqual(_file.unpacked_url, os.path.join(settings.MEDIA_URL, os.path.splitext(_file.name)[0]))
        unpacked_path = _file.unpacked_path
        self.assertTrue(os.path.exists(unpacked_path))

        _file.delete(save=False)

        self.assertFalse(_file.unpacked_path)
        self.assertFalse(os.path.exists(unpacked_path))
