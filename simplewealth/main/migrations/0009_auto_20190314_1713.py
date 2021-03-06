# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-14 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190314_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Users')),
                ('TD', models.PositiveSmallIntegerField(default=0)),
                ('JPM', models.PositiveSmallIntegerField(default=0)),
                ('V', models.PositiveSmallIntegerField(default=0)),
                ('BRKB', models.PositiveSmallIntegerField(default=0)),
                ('AAPL', models.PositiveSmallIntegerField(default=0)),
                ('MSFT', models.PositiveSmallIntegerField(default=0)),
                ('AMZN', models.PositiveSmallIntegerField(default=0)),
                ('FB', models.PositiveSmallIntegerField(default=0)),
                ('ENB', models.PositiveSmallIntegerField(default=0)),
                ('TRP', models.PositiveSmallIntegerField(default=0)),
                ('XOM', models.PositiveSmallIntegerField(default=0)),
                ('CVX', models.PositiveSmallIntegerField(default=0)),
                ('BA', models.PositiveSmallIntegerField(default=0)),
                ('UNP', models.PositiveSmallIntegerField(default=0)),
                ('UTX', models.PositiveSmallIntegerField(default=0)),
                ('TSLA', models.PositiveSmallIntegerField(default=0)),
                ('PG', models.PositiveSmallIntegerField(default=0)),
                ('KO', models.PositiveSmallIntegerField(default=0)),
                ('MCD', models.PositiveSmallIntegerField(default=0)),
                ('WMT', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
