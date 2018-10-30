# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20181026_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='单价'),
        ),
    ]