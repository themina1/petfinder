# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('animal', models.CharField(max_length=20, blank=True)),
                ('petId', models.CharField(max_length=20, serialize=False, verbose_name=b'ID', primary_key=True, blank=True)),
                ('firstSeen', models.DateTimeField(null=True, verbose_name=b'First Seen')),
                ('lastSeen', models.DateTimeField(null=True, verbose_name=b'Last seen ')),
                ('petName', models.CharField(max_length=50, verbose_name=b'Name: ', blank=True)),
                ('petDescription', models.TextField(verbose_name=b'Description', blank=True)),
                ('petBreed', models.CharField(max_length=100, verbose_name=b'Breed', blank=True)),
                ('petStatus', models.CharField(max_length=10, verbose_name=b'Status', blank=True)),
                ('petAge', models.CharField(max_length=10, verbose_name=b'Age', blank=True)),
                ('petSex', models.CharField(max_length=10, verbose_name=b'Sex', blank=True)),
                ('petSize', models.CharField(max_length=10, verbose_name=b'Size', blank=True)),
                ('petMix', models.CharField(max_length=10, verbose_name=b'Mixed?', blank=True)),
                ('petFeatures', models.CharField(max_length=200, verbose_name=b'Features', blank=True)),
                ('petPhoto', models.TextField(verbose_name=b'Picture', blank=True)),
                ('address', models.CharField(default=b'10 Animal Place', max_length=200, blank=True)),
                ('city', models.CharField(default=b'Lexington', max_length=50, blank=True)),
                ('email', models.CharField(default=b'shelter@rockbridgespca.net', max_length=200, blank=True)),
                ('fax', models.CharField(default=b'540-464-8847', max_length=200, blank=True)),
                ('phone', models.CharField(default=b'540-463-5123', max_length=200, blank=True)),
                ('state', models.CharField(default=b'VA', max_length=2)),
                ('zip', models.CharField(default=b'24450', max_length=10)),
                ('match', models.CharField(default=b'No', max_length=5)),
                ('newField', models.CharField(default=b'1', max_length=1)),
            ],
            options={
                'ordering': ['petId'],
            },
        ),
    ]
