# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0008_auto_20160411_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='user_id',
            field=models.IntegerField(max_length=15),
            preserve_default=True,
        ),
    ]
