# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-13 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0007_auto_20171213_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='outer_ip',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='outer ip'),
        ),
    ]