# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RideSharing', '0003_auto_20160406_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='newride',
            name='rate',
            field=models.IntegerField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='waypoints',
            name='rate',
            field=models.IntegerField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
    ]
