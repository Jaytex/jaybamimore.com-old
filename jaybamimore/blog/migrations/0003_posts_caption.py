# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160508_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='caption',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
