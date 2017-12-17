# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-13 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0003_auto_20171213_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='liked_by',
            field=models.ManyToManyField(default='', related_name='liked_books', to='book_authors.User'),
        ),
    ]