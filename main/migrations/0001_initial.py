# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlideImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='slides_img')),
                ('url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
