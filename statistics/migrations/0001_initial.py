# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RideOffer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('weekday', models.IntegerField(max_length=1)),
                ('time', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='rideSearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('date_time', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
