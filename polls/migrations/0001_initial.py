# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82')),
                ('answer_true', models.BooleanField(verbose_name=b'\xd0\x92\xd0\xb5\xd1\x80\xd0\xbd\xd0\xbe?')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\xa2\xd0\xb8\xd1\x82\xd1\x83\xd0\xbb')),
                ('text', models.TextField(verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
