# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20170316_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='savetest',
            name='fio',
            field=models.CharField(max_length=80, null=True, verbose_name=b'\xd0\xa4\xd0\x98\xd0\x9e'),
        ),
        migrations.AddField(
            model_name='savetest',
            name='position',
            field=models.CharField(max_length=80, null=True, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbb\xd0\xb6\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c'),
        ),
    ]
