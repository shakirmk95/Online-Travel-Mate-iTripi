# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0005_auto_20160408_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transportimage',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='TransportImage',
        ),
        migrations.AddField(
            model_name='transport',
            name='image',
            field=models.ImageField(default=b'default.jpg', upload_to=b'car/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
