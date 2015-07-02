# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petfind', '0004_remove_animal_newfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='newField',
            field=models.CharField(default=b'1', max_length=1),
        ),
    ]
