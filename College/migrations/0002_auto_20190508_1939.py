# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-08 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffregistration',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
