# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0003_auto_20160408_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='image',
            field=models.ImageField(default='', upload_to=b'Transport/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
