# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0011_remove_transport_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='color',
            field=models.CharField(default=b'Green', max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
    ]
