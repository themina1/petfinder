# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petfind', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='commoninfo_ptr',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='dogId',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='catId',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='commoninfo_ptr',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='unique',
            name='commoninfo_ptr',
        ),
        migrations.RemoveField(
            model_name='unique',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='unique',
            name='uniqueId',
        ),
        migrations.AddField(
            model_name='cat',
            name='address1',
            field=models.CharField(max_length=50, verbose_name=b'Address1', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='address2',
            field=models.CharField(max_length=50, verbose_name=b'Address2', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='city',
            field=models.CharField(max_length=50, verbose_name=b'City', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='email',
            field=models.CharField(max_length=50, verbose_name=b'E-Mail', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='fax',
            field=models.CharField(max_length=50, verbose_name=b'Fax', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='id',
            field=models.IntegerField(default=0, unique=True, serialize=False, verbose_name=b'id', primary_key=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='phone',
            field=models.CharField(max_length=50, verbose_name=b'Phone', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='state',
            field=models.CharField(max_length=2, verbose_name=b'State', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='zip',
            field=models.CharField(max_length=5, verbose_name=b'Zip Code', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='address1',
            field=models.CharField(max_length=50, verbose_name=b'Address1', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='address2',
            field=models.CharField(max_length=50, verbose_name=b'Address2', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='city',
            field=models.CharField(max_length=50, verbose_name=b'City', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='email',
            field=models.CharField(max_length=50, verbose_name=b'E-Mail', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='fax',
            field=models.CharField(max_length=50, verbose_name=b'Fax', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='id',
            field=models.IntegerField(default=0, unique=True, serialize=False, verbose_name=b'id', primary_key=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='phone',
            field=models.CharField(max_length=50, verbose_name=b'Phone', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='state',
            field=models.CharField(max_length=2, verbose_name=b'State', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='zip',
            field=models.CharField(max_length=5, verbose_name=b'Zip Code', blank=True),
        ),
        migrations.AddField(
            model_name='unique',
            name='address1',
            field=models.CharField(max_length=50, verbose_name=b'Address1', blank=True),
        ),
        migrations.AddField(
            model_name='unique',
            name='address2',
            field=models.CharField(max_length=50, verbose_name=b'Address2', blank=True),
        ),
        migrations.AddField(
            model_name='unique',
            name='city',
            field=models.CharField(max_length=50, verbose_name=b'City', blank=True),
        ),
        migrations.AddField(
            model_name='unique',
            name='email',
            field=models.CharField(max_length=50, verbose_name=b'E-Mail', blank=True),
        ),
        migrations.AddField(
            model_name='unique',
            name='fax',
            field=models.CharField(max_length=50, verbose_name=b'Fax', blank=True),
        ),
        migrations.AddField(
            model_name='unique',
            name='id',
            field=models.IntegerField(default=0, unique=True, serialize=False, verbose_name=b'id', primary_key=True),
        ),
        migrations.AddField(
            model_name='unique',
            name='phone',
            field=models.CharField(max_length=50, verbose_name=b'Phone', blank=True),
        ),
        migrations.AddField(
            model_name='unique',
            name='state',
            field=models.CharField(max_length=2, verbose_name=b'State', blank=True),
        ),
        migrations.AddField(
            model_name='unique',
            name='zip',
            field=models.CharField(max_length=5, verbose_name=b'Zip Code', blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='age',
            field=models.CharField(max_length=50, verbose_name=b'Age', blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='breeds',
            field=models.CharField(max_length=50, verbose_name=b'Breeds', blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='description',
            field=models.TextField(verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='media',
            field=models.TextField(verbose_name=b'Media', blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='mix',
            field=models.CharField(max_length=50, verbose_name=b'Mix', blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'Name', blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='options',
            field=models.CharField(max_length=50, verbose_name=b'Options', blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='sex',
            field=models.CharField(max_length=50, verbose_name=b'Sex', blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='shelterId',
            field=models.CharField(max_length=50, verbose_name=b'ShelterID', blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='shelterPetId',
            field=models.CharField(max_length=50, verbose_name=b'ShelterPetID', blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='size',
            field=models.CharField(max_length=50, verbose_name=b'Size', blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='status',
            field=models.CharField(max_length=50, verbose_name=b'Status', blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.CharField(max_length=50, verbose_name=b'Age', blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='breeds',
            field=models.CharField(max_length=50, verbose_name=b'Breeds', blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='description',
            field=models.TextField(verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='media',
            field=models.TextField(verbose_name=b'Media', blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='mix',
            field=models.CharField(max_length=50, verbose_name=b'Mix', blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'Name', blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='options',
            field=models.CharField(max_length=50, verbose_name=b'Options', blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='sex',
            field=models.CharField(max_length=50, verbose_name=b'Sex', blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='shelterId',
            field=models.CharField(max_length=50, verbose_name=b'ShelterID', blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='shelterPetId',
            field=models.CharField(max_length=50, verbose_name=b'ShelterPetID', blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='size',
            field=models.CharField(max_length=50, verbose_name=b'Size', blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='status',
            field=models.CharField(max_length=50, verbose_name=b'Status', blank=True),
        ),
        migrations.AlterField(
            model_name='unique',
            name='age',
            field=models.CharField(max_length=50, verbose_name=b'Age', blank=True),
        ),
        migrations.AlterField(
            model_name='unique',
            name='breeds',
            field=models.CharField(max_length=50, verbose_name=b'Breeds', blank=True),
        ),
        migrations.AlterField(
            model_name='unique',
            name='description',
            field=models.TextField(verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='unique',
            name='media',
            field=models.TextField(verbose_name=b'Media', blank=True),
        ),
        migrations.AlterField(
            model_name='unique',
            name='mix',
            field=models.CharField(max_length=50, verbose_name=b'Mix', blank=True),
        ),
        migrations.AlterField(
            model_name='unique',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'Name', blank=True),
        ),
        migrations.AlterField(
            model_name='unique',
            name='options',
            field=models.CharField(max_length=50, verbose_name=b'Options', blank=True),
        ),
        migrations.AlterField(
            model_name='unique',
            name='sex',
            field=models.CharField(max_length=50, verbose_name=b'Sex', blank=True),
        ),
        migrations.AlterField(
            model_name='unique',
            name='shelterId',
            field=models.CharField(max_length=50, verbose_name=b'ShelterID', blank=True),
        ),
        migrations.AlterField(
            model_name='unique',
            name='shelterPetId',
            field=models.CharField(max_length=50, verbose_name=b'ShelterPetID', blank=True),
        ),
        migrations.AlterField(
            model_name='unique',
            name='size',
            field=models.CharField(max_length=50, verbose_name=b'Size', blank=True),
        ),
        migrations.AlterField(
            model_name='unique',
            name='status',
            field=models.CharField(max_length=50, verbose_name=b'Status', blank=True),
        ),
        migrations.DeleteModel(
            name='CommonInfo',
        ),
    ]
