# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-05 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_news', '0003_auto_20161105_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='newswebsite',
            name='phantomjs_wait',
            field=models.IntegerField(default=0),
        ),
    ]
