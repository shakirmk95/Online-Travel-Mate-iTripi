# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0009_auto_20160414_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='trans_rating',
            field=models.IntegerField(default=1, max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
    ]
