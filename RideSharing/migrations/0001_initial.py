# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='newRide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_id', models.IntegerField(max_length=50)),
                ('origin', models.CharField(max_length=150)),
                ('destination', models.CharField(max_length=150)),
                ('luggage', models.CharField(max_length=1, null=True, blank=True)),
                ('seats', models.IntegerField(max_length=1)),
                ('detour', models.CharField(max_length=3, null=True, blank=True)),
                ('datetime', models.DateTimeField()),
                ('date_published', models.DateField()),
                ('description', models.CharField(max_length=256)),
                ('cus_url', models.CharField(max_length=21)),
                ('seen', models.IntegerField(default=0, max_length=3)),
                ('vehicle_id', models.CharField(max_length=5, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='requestedUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'N', max_length=1)),
                ('time_of_approval', models.DateTimeField(null=True, blank=True)),
                ('cus_url', models.CharField(max_length=21)),
                ('host_id', models.ForeignKey(related_name='host_id', to=settings.AUTH_USER_MODEL)),
                ('ride_id', models.ForeignKey(to='RideSharing.newRide')),
                ('user_id', models.ForeignKey(related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='wayPoints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ride_id', models.IntegerField(max_length=50)),
                ('point', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=50)),
                ('reaching_time', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
