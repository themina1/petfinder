# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petfind', '0006_remove_animal_newfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedditPost',
            fields=[
                ('post_id', models.CharField(default=b'0', max_length=20, serialize=False, verbose_name=b'Id', primary_key=True)),
                ('link', models.TextField(verbose_name=b'Link', blank=True)),
                ('title', models.TextField(verbose_name=b'Title', blank=True)),
                ('up_votes', models.CharField(max_length=20, verbose_name=b'Up Votes', blank=True)),
                ('img', models.TextField(verbose_name=b'Image', blank=True)),
            ],
        ),
    ]
