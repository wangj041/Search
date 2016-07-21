# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WangBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.FileField(default='', upload_to='./upload/'),
        ),
    ]