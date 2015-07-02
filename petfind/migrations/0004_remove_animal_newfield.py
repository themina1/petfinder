# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petfind', '0003_animal_petphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='newField',
        ),
    ]
