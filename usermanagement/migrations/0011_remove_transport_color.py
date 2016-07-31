# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0010_auto_20160414_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='color',
        ),
    ]
