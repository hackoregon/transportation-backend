# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIimports', '0003_auto_20170414_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='orig_status',
            field=models.CharField(blank=True, max_length=2083, null=True),
        ),
    ]
