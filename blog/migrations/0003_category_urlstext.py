# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='urlstext',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
