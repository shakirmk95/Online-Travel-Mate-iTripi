# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RideSharing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car_id', models.IntegerField(max_length=100)),
                ('voters_id', models.IntegerField(max_length=100)),
                ('rating', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=1000)),
                ('has_read', models.IntegerField(default=0, max_length=1)),
                ('sent_time', models.DateTimeField(null=True, blank=True)),
                ('read_time', models.DateTimeField(null=True, blank=True)),
                ('cus_url', models.CharField(max_length=21)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RideReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ride_id', models.CharField(max_length=100)),
                ('voters_id', models.CharField(max_length=100)),
                ('review_descriprion', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('make', models.CharField(max_length=15)),
                ('car', models.CharField(max_length=15)),
                ('varient', models.CharField(max_length=15)),
                ('color', models.CharField(max_length=15)),
                ('comfort', models.CharField(max_length=15, choices=[(b'B', b'Basic'), (b'N', b'Normal'), (b'L', b'Luxuary'), (b'C', b'Comfortable')])),
                ('seats', models.IntegerField(max_length=1)),
                ('trans_rating', models.IntegerField(default=0, max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('user_id', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(default=b'default.jpg', upload_to=b'documents/%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserNotifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target_user', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=256)),
                ('has_read', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_id', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mobile', models.CharField(max_length=15)),
                ('phone_visiblity', models.CharField(default=b'Y', max_length=1)),
                ('yob', models.IntegerField(max_length=4, null=True, blank=True)),
                ('work', models.CharField(max_length=120)),
                ('bio', models.CharField(max_length=256)),
                ('add1', models.CharField(default=b'', max_length=250)),
                ('add2', models.CharField(default=b'', max_length=250)),
                ('zip_code', models.CharField(max_length=8)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=20)),
                ('user_rating', models.IntegerField(default=0, max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(max_length=100)),
                ('voters_id', models.IntegerField(max_length=100)),
                ('rating', models.IntegerField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='transport',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messages',
            name='reciever',
            field=models.ForeignKey(related_name='reciever', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messages',
            name='ride_link',
            field=models.ForeignKey(related_name='ride_id', to='RideSharing.newRide'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messages',
            name='sender',
            field=models.ForeignKey(related_name='sender', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
