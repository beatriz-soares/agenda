# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('idade', models.PositiveIntegerField()),
                ('site', models.URLField()),
                ('datacadastro', models.DateField()),
            ],
        ),
    ]
