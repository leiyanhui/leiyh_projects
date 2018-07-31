# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 15:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freshmarket', '0004_auto_20180620_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_phone',
        ),
        migrations.AlterField(
            model_name='address',
            name='address_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 20, 23, 33, 50, 104832)),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 20, 23, 33, 50, 103831)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 20, 23, 33, 50, 104832)),
        ),
        migrations.AlterField(
            model_name='product_picture',
            name='picture_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 20, 23, 33, 50, 102835)),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_crate_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 20, 23, 33, 50, 102835)),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scan_datatime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 20, 23, 33, 50, 103831)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_crate_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 20, 23, 33, 50, 101839)),
        ),
    ]