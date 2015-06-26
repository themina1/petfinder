# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('petfind', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueAnimal',
            fields=[
                ('petId', models.CharField(default=0, max_length=10, serialize=False, verbose_name=b'ID', primary_key=True)),
                ('petName', models.CharField(max_length=20, verbose_name=b'Name: ', blank=True)),
                ('timeInShelter', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'In shelter since ')),
                ('petDescription', models.TextField(verbose_name=b'Description', blank=True)),
                ('petBreed', models.CharField(max_length=100, verbose_name=b'Breed', blank=True)),
                ('petStatus', models.CharField(max_length=50, verbose_name=b'Status', blank=True)),
                ('petAge', models.CharField(max_length=10, verbose_name=b'Age', blank=True)),
                ('petSex', models.CharField(max_length=10, verbose_name=b'Sex', blank=True)),
                ('petSize', models.CharField(max_length=10, verbose_name=b'Size', blank=True)),
                ('petMix', models.CharField(max_length=10, verbose_name=b'Mixed?', blank=True)),
                ('petFeatures', models.CharField(max_length=100, verbose_name=b'Features', blank=True)),
                ('address', models.CharField(default=b'10 Animal Place', max_length=200, blank=True)),
                ('city', models.CharField(default=b'Lexington', max_length=50, blank=True)),
                ('email', models.CharField(default=b'shelter@rockbridgespca.net', max_length=200, blank=True)),
                ('fax', models.CharField(default=b'540-464-8847', max_length=200, blank=True)),
                ('phone', models.CharField(default=b'540-463-5123', max_length=200, blank=True)),
                ('state', models.CharField(default=b'VA', max_length=2, blank=True)),
                ('zip', models.CharField(default=b'24450', max_length=10, blank=True)),
                ('uniqueAnimal', models.CharField(max_length=15, blank=True)),
            ],
            options={
                'ordering': ['petId'],
            },
        ),
        migrations.DeleteModel(
            name='Unique',
        ),
        migrations.AlterModelOptions(
            name='cat',
            options={'ordering': ['petId']},
        ),
        migrations.AlterModelOptions(
            name='dog',
            options={'ordering': ['petId']},
        ),
        migrations.RenameField(
            model_name='cat',
            old_name='description',
            new_name='petDescription',
        ),
        migrations.RenameField(
            model_name='cat',
            old_name='status',
            new_name='petStatus',
        ),
        migrations.RenameField(
            model_name='dog',
            old_name='description',
            new_name='petDescription',
        ),
        migrations.RenameField(
            model_name='dog',
            old_name='status',
            new_name='petStatus',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='age',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='breeds',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='lastUpdate',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='media',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='mix',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='options',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='shelterId',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='shelterPetId',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='size',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='age',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='breeds',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='id',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='lastUpdate',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='media',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='mix',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='name',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='options',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='shelterId',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='shelterPetId',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='size',
        ),
        migrations.AddField(
            model_name='cat',
            name='address',
            field=models.CharField(default=b'10 Animal Place', max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='petAge',
            field=models.CharField(max_length=10, verbose_name=b'Age', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='petBreed',
            field=models.CharField(max_length=100, verbose_name=b'Breed', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='petFeatures',
            field=models.CharField(max_length=100, verbose_name=b'Features', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='petId',
            field=models.CharField(default=0, max_length=10, serialize=False, verbose_name=b'ID', primary_key=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='petMix',
            field=models.CharField(max_length=10, verbose_name=b'Mixed?', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='petName',
            field=models.CharField(max_length=20, verbose_name=b'Name: ', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='petSex',
            field=models.CharField(max_length=10, verbose_name=b'Sex', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='petSize',
            field=models.CharField(max_length=10, verbose_name=b'Size', blank=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='timeInShelter',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'In shelter since '),
        ),
        migrations.AddField(
            model_name='dog',
            name='address',
            field=models.CharField(default=b'10 Animal Place', max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='petAge',
            field=models.CharField(max_length=10, verbose_name=b'Age', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='petBreed',
            field=models.CharField(max_length=100, verbose_name=b'Breed', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='petFeatures',
            field=models.CharField(max_length=100, verbose_name=b'Features', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='petId',
            field=models.CharField(default=0, max_length=10, serialize=False, verbose_name=b'ID', primary_key=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='petMix',
            field=models.CharField(max_length=10, verbose_name=b'Mixed?', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='petName',
            field=models.CharField(max_length=20, verbose_name=b'Name: ', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='petSex',
            field=models.CharField(max_length=10, verbose_name=b'Sex', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='petSize',
            field=models.CharField(max_length=10, verbose_name=b'Size', blank=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='timeInShelter',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'In shelter since '),
        ),
        migrations.AlterField(
            model_name='cat',
            name='city',
            field=models.CharField(default=b'Lexington', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='email',
            field=models.CharField(default=b'shelter@rockbridgespca.net', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='fax',
            field=models.CharField(default=b'540-464-8847', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='phone',
            field=models.CharField(default=b'540-463-5123', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='state',
            field=models.CharField(default=b'VA', max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='zip',
            field=models.CharField(default=b'24450', max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='city',
            field=models.CharField(default=b'Lexington', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='email',
            field=models.CharField(default=b'shelter@rockbridgespca.net', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='fax',
            field=models.CharField(default=b'540-464-8847', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='phone',
            field=models.CharField(default=b'540-463-5123', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='state',
            field=models.CharField(default=b'VA', max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='zip',
            field=models.CharField(default=b'24450', max_length=10, blank=True),
        ),
    ]
