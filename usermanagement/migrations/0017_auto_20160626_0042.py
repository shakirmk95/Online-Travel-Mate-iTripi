# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0016_auto_20160625_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='orginal_image_url',
            new_name='original_image_url',
        ),
    ]
