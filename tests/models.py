from django.db import models

from archive_field.fields import ArchiveFileField


class TestModel(models.Model):
    archive = ArchiveFileField(upload_to='test_archive')
