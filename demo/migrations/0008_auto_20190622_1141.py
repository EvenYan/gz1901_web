# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-22 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20190622_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='people',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='demo.People'),
        ),
    ]
