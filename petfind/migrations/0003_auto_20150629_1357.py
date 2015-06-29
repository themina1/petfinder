# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petfind', '0002_auto_20150624_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='timeInShelter',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='timeInShelter',
        ),
        migrations.RemoveField(
            model_name='uniqueanimal',
            name='timeInShelter',
        ),
        migrations.AddField(
            model_name='cat',
            name='firstSeen',
            field=models.DateTimeField(null=True, verbose_name=b'First Seen'),
        ),
        migrations.AddField(
            model_name='cat',
            name='lastSeen',
            field=models.DateTimeField(null=True, verbose_name=b'Last seen '),
        ),
        migrations.AddField(
            model_name='dog',
            name='firstSeen',
            field=models.DateTimeField(null=True, verbose_name=b'First Seen'),
        ),
        migrations.AddField(
            model_name='dog',
            name='lastSeen',
            field=models.DateTimeField(null=True, verbose_name=b'Last seen '),
        ),
        migrations.AddField(
            model_name='uniqueanimal',
            name='firstSeen',
            field=models.DateTimeField(null=True, verbose_name=b'First Seen'),
        ),
        migrations.AddField(
            model_name='uniqueanimal',
            name='lastSeen',
            field=models.DateTimeField(null=True, verbose_name=b'Last seen '),
        ),
    ]
