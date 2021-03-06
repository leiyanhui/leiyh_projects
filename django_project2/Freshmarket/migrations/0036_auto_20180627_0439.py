# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 20:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Freshmarket', '0035_auto_20180627_0424'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='order',
            managers=[
                ('order_object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_post_spend',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_total_spend',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='address_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 27, 4, 39, 20, 593247)),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 27, 4, 39, 20, 593247)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 27, 4, 39, 20, 594241)),
        ),
        migrations.AlterField(
            model_name='product_picture',
            name='picture_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 27, 4, 39, 20, 591249)),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_crate_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 27, 4, 39, 20, 591249)),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scan_datatime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 27, 4, 39, 20, 592346)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_crate_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 27, 4, 39, 20, 590304)),
        ),
    ]
