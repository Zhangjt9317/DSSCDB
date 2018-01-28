# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-28 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dye', '0002_auto_20171023_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='molecule',
            name='representation_3d',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='molecule',
            name='inchi',
            field=models.CharField(max_length=1000, unique=True, verbose_name='InChI'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='dye_loading',
            field=models.CharField(blank=True, help_text='[nmol/cm2]', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='exposure_time',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]