# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0002_auto_20160406_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='color',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transport',
            name='comfort',
            field=models.CharField(blank=True, max_length=15, null=True, choices=[(b'B', b'Basic'), (b'N', b'Normal'), (b'L', b'Luxuary'), (b'C', b'Comfortable')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transport',
            name='trans_rating',
            field=models.IntegerField(default=0, max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
    ]
