# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0006_auto_20160408_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='image',
            field=models.ImageField(default=b'default.jpg', null=True, upload_to=b'car/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
