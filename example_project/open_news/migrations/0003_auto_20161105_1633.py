# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-05 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_news', '0002_newswebsite_allowed_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newswebsite',
            name='allowed_domain',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]