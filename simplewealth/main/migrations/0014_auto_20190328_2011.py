# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-28 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190328_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='risk_status',
            field=models.CharField(choices=[(b'hi', b'High'), (b'med', b'Medium'), (b'lo', b'Low')], default=b'med', max_length=2),
        ),
    ]
