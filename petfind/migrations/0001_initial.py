# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address1', models.CharField(max_length=50, verbose_name=b'Address1')),
                ('address2', models.CharField(max_length=50, verbose_name=b'Address2')),
                ('city', models.CharField(max_length=50, verbose_name=b'City')),
                ('email', models.CharField(max_length=50, verbose_name=b'E-Mail')),
                ('fax', models.CharField(max_length=50, verbose_name=b'Fax')),
                ('phone', models.CharField(max_length=50, verbose_name=b'Phone')),
                ('state', models.CharField(max_length=2, verbose_name=b'State')),
                ('zip', models.CharField(max_length=5, verbose_name=b'Zip Code')),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='petfind.CommonInfo')),
                ('age', models.CharField(max_length=50, verbose_name=b'Age')),
                ('animal', models.CharField(max_length=50, verbose_name=b'Animal')),
                ('breeds', models.CharField(max_length=50, verbose_name=b'Breeds')),
                ('contact', models.TextField(verbose_name=b'Contact')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('dogId', models.IntegerField(default=0, verbose_name=b'id')),
                ('lastUpdate', models.DateTimeField(default=None, null=True, verbose_name=b'Date of Last Update', blank=True)),
                ('media', models.TextField(verbose_name=b'Media')),
                ('mix', models.CharField(max_length=50, verbose_name=b'Mix')),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('options', models.CharField(max_length=50, verbose_name=b'Options')),
                ('sex', models.CharField(max_length=50, verbose_name=b'Sex')),
                ('shelterId', models.CharField(max_length=50, verbose_name=b'ShelterID')),
                ('shelterPetId', models.CharField(max_length=50, verbose_name=b'ShelterPetID')),
                ('size', models.CharField(max_length=50, verbose_name=b'Size')),
                ('status', models.CharField(max_length=50, verbose_name=b'Status')),
            ],
            bases=('petfind.commoninfo',),
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='petfind.CommonInfo')),
                ('age', models.CharField(max_length=50, verbose_name=b'Age')),
                ('animal', models.CharField(max_length=50, verbose_name=b'Animal')),
                ('breeds', models.CharField(max_length=50, verbose_name=b'Breeds')),
                ('contact', models.TextField(verbose_name=b'Contact')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('catId', models.IntegerField(default=0, verbose_name=b'id')),
                ('lastUpdate', models.DateTimeField(default=None, null=True, verbose_name=b'Date of Last Update', blank=True)),
                ('media', models.TextField(verbose_name=b'Media')),
                ('mix', models.CharField(max_length=50, verbose_name=b'Mix')),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('options', models.CharField(max_length=50, verbose_name=b'Options')),
                ('sex', models.CharField(max_length=50, verbose_name=b'Sex')),
                ('shelterId', models.CharField(max_length=50, verbose_name=b'ShelterID')),
                ('shelterPetId', models.CharField(max_length=50, verbose_name=b'ShelterPetID')),
                ('size', models.CharField(max_length=50, verbose_name=b'Size')),
                ('status', models.CharField(max_length=50, verbose_name=b'Status')),
            ],
            bases=('petfind.commoninfo',),
        ),
        migrations.CreateModel(
            name='Unique',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='petfind.CommonInfo')),
                ('age', models.CharField(max_length=50, verbose_name=b'Age')),
                ('animal', models.CharField(max_length=50, verbose_name=b'Animal')),
                ('breeds', models.CharField(max_length=50, verbose_name=b'Breeds')),
                ('contact', models.TextField(verbose_name=b'Contact')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('uniqueId', models.IntegerField(default=0, verbose_name=b'id')),
                ('lastUpdate', models.DateTimeField(default=None, null=True, verbose_name=b'Date of Last Update', blank=True)),
                ('media', models.TextField(verbose_name=b'Media')),
                ('mix', models.CharField(max_length=50, verbose_name=b'Mix')),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('options', models.CharField(max_length=50, verbose_name=b'Options')),
                ('sex', models.CharField(max_length=50, verbose_name=b'Sex')),
                ('shelterId', models.CharField(max_length=50, verbose_name=b'ShelterID')),
                ('shelterPetId', models.CharField(max_length=50, verbose_name=b'ShelterPetID')),
                ('size', models.CharField(max_length=50, verbose_name=b'Size')),
                ('status', models.CharField(max_length=50, verbose_name=b'Status')),
            ],
            bases=('petfind.commoninfo',),
        ),
    ]
