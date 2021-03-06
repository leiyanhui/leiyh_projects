# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 08:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freshmarket', '0022_auto_20180625_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 16, 31, 14, 613708)),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 25, 16, 31, 14, 612710)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 16, 31, 14, 613708)),
        ),
        migrations.AlterField(
            model_name='order_products',
            name='op_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 16, 31, 14, 614711)),
        ),
        migrations.AlterField(
            model_name='product_picture',
            name='picture_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 16, 31, 14, 611713)),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_crate_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 16, 31, 14, 611713)),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scan_datatime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 16, 31, 14, 612710)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_crate_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 16, 31, 14, 610715)),
        ),
    ]
