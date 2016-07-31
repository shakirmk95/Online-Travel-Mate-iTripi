# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('RideSharing', '0002_auto_20160406_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newride',
            name='host_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
