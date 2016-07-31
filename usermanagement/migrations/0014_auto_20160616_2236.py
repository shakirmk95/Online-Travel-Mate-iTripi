# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0013_auto_20160616_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(default=b'default.jpg', upload_to=b'documents/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
