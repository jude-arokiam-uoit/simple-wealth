# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-11 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('symbol', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=50)),
            ],
        ),
    ]
