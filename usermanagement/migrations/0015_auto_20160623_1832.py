# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0014_auto_20160616_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(default=b'default.jpg', upload_to=b'profile_pic'),
            preserve_default=True,
        ),
    ]
