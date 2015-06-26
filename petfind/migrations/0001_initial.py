# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('age', models.CharField(max_length=50, verbose_name=b'Age', blank=True)),
                ('breeds', models.CharField(max_length=50, verbose_name=b'Breeds', blank=True)),
                ('address1', models.CharField(max_length=50, verbose_name=b'Address1', blank=True)),
                ('address2', models.CharField(max_length=50, verbose_name=b'Address2', blank=True)),
                ('city', models.CharField(max_length=50, verbose_name=b'City', blank=True)),
                ('email', models.CharField(max_length=50, verbose_name=b'E-Mail', blank=True)),
                ('fax', models.CharField(max_length=50, verbose_name=b'Fax', blank=True)),
                ('phone', models.CharField(max_length=50, verbose_name=b'Phone', blank=True)),
                ('state', models.CharField(max_length=2, verbose_name=b'State', blank=True)),
                ('zip', models.CharField(max_length=5, verbose_name=b'Zip Code', blank=True)),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('id', models.CharField(primary_key=True, default=0, serialize=False, max_length=50, unique=True, verbose_name=b'ID')),
                ('lastUpdate', models.DateTimeField(default=None, null=True, verbose_name=b'Date of Last Update', blank=True)),
                ('media', models.TextField(verbose_name=b'Media', blank=True)),
                ('mix', models.CharField(max_length=50, verbose_name=b'Mix', blank=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name', blank=True)),
                ('options', models.CharField(max_length=50, verbose_name=b'Options', blank=True)),
                ('sex', models.CharField(max_length=50, verbose_name=b'Sex', blank=True)),
                ('shelterId', models.CharField(max_length=50, verbose_name=b'ShelterID', blank=True)),
                ('shelterPetId', models.CharField(max_length=50, verbose_name=b'ShelterPetID', blank=True)),
                ('size', models.CharField(max_length=50, verbose_name=b'Size', blank=True)),
                ('status', models.CharField(max_length=50, verbose_name=b'Status', blank=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('age', models.CharField(max_length=50, verbose_name=b'Age', blank=True)),
                ('breeds', models.CharField(max_length=50, verbose_name=b'Breeds', blank=True)),
                ('address1', models.CharField(max_length=50, verbose_name=b'Address1', blank=True)),
                ('address2', models.CharField(max_length=50, verbose_name=b'Address2', blank=True)),
                ('city', models.CharField(max_length=50, verbose_name=b'City', blank=True)),
                ('email', models.CharField(max_length=50, verbose_name=b'E-Mail', blank=True)),
                ('fax', models.CharField(max_length=50, verbose_name=b'Fax', blank=True)),
                ('phone', models.CharField(max_length=50, verbose_name=b'Phone', blank=True)),
                ('state', models.CharField(max_length=2, verbose_name=b'State', blank=True)),
                ('zip', models.CharField(max_length=5, verbose_name=b'Zip Code', blank=True)),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('id', models.CharField(primary_key=True, default=0, serialize=False, max_length=50, unique=True, verbose_name=b'ID')),
                ('lastUpdate', models.DateTimeField(default=None, null=True, verbose_name=b'Date of Last Update', blank=True)),
                ('media', models.TextField(verbose_name=b'Media', blank=True)),
                ('mix', models.CharField(max_length=50, verbose_name=b'Mix', blank=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name', blank=True)),
                ('options', models.CharField(max_length=50, verbose_name=b'Options', blank=True)),
                ('sex', models.CharField(max_length=50, verbose_name=b'Sex', blank=True)),
                ('shelterId', models.CharField(max_length=50, verbose_name=b'ShelterID', blank=True)),
                ('shelterPetId', models.CharField(max_length=50, verbose_name=b'ShelterPetID', blank=True)),
                ('size', models.CharField(max_length=50, verbose_name=b'Size', blank=True)),
                ('status', models.CharField(max_length=50, verbose_name=b'Status', blank=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Unique',
            fields=[
                ('age', models.CharField(max_length=50, verbose_name=b'Age', blank=True)),
                ('breeds', models.CharField(max_length=50, verbose_name=b'Breeds', blank=True)),
                ('address1', models.CharField(max_length=50, verbose_name=b'Address1', blank=True)),
                ('address2', models.CharField(max_length=50, verbose_name=b'Address2', blank=True)),
                ('city', models.CharField(max_length=50, verbose_name=b'City', blank=True)),
                ('email', models.CharField(max_length=50, verbose_name=b'E-Mail', blank=True)),
                ('fax', models.CharField(max_length=50, verbose_name=b'Fax', blank=True)),
                ('phone', models.CharField(max_length=50, verbose_name=b'Phone', blank=True)),
                ('state', models.CharField(max_length=2, verbose_name=b'State', blank=True)),
                ('zip', models.CharField(max_length=5, verbose_name=b'Zip Code', blank=True)),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('id', models.CharField(primary_key=True, default=0, serialize=False, max_length=50, unique=True, verbose_name=b'ID')),
                ('lastUpdate', models.DateTimeField(default=None, null=True, verbose_name=b'Date of Last Update', blank=True)),
                ('media', models.TextField(verbose_name=b'Media', blank=True)),
                ('mix', models.CharField(max_length=50, verbose_name=b'Mix', blank=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name', blank=True)),
                ('options', models.CharField(max_length=50, verbose_name=b'Options', blank=True)),
                ('sex', models.CharField(max_length=50, verbose_name=b'Sex', blank=True)),
                ('shelterId', models.CharField(max_length=50, verbose_name=b'ShelterID', blank=True)),
                ('shelterPetId', models.CharField(max_length=50, verbose_name=b'ShelterPetID', blank=True)),
                ('size', models.CharField(max_length=50, verbose_name=b'Size', blank=True)),
                ('status', models.CharField(max_length=50, verbose_name=b'Status', blank=True)),
                ('animal', models.CharField(max_length=50, verbose_name=b'Animal', blank=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
