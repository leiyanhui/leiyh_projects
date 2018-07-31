# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 07:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freshmarket', '0019_auto_20180625_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 15, 13, 56, 89420)),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 25, 15, 13, 56, 88423)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 15, 13, 56, 89420)),
        ),
        migrations.AlterField(
            model_name='order_products',
            name='op_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 15, 13, 56, 90418)),
        ),
        migrations.AlterField(
            model_name='product_picture',
            name='picture_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 15, 13, 56, 87426)),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_crate_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 15, 13, 56, 86429)),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scan_datatime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 15, 13, 56, 87426)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_crate_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 15, 13, 56, 86429)),
        ),
    ]