# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RideSharing', '0004_auto_20160415_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='newride',
            name='distance',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waypoints',
            name='distance',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
    ]
