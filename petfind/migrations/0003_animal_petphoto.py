# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petfind', '0002_remove_animal_petphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='petPhoto',
            field=models.TextField(verbose_name=b'Picture', blank=True),
        ),
    ]
