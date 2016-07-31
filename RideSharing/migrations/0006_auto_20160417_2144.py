# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RideSharing', '0005_auto_20160417_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newride',
            name='distance',
        ),
        migrations.RemoveField(
            model_name='waypoints',
            name='distance',
        ),
    ]
