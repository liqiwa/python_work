# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-14 16:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzerias', '0002_auto_20181228_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'toppings'},
        ),
    ]
