# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 06:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Freshmarket', '0017_auto_20180625_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_pro_foreignkey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Freshmarket.Order_Products'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='address_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 14, 37, 18, 795575)),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 25, 14, 37, 18, 794552)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 14, 37, 18, 796575)),
        ),
        migrations.AlterField(
            model_name='order_products',
            name='op_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 14, 37, 18, 796575)),
        ),
        migrations.AlterField(
            model_name='product_picture',
            name='picture_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 14, 37, 18, 793555)),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_crate_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 14, 37, 18, 793555)),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scan_datatime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 14, 37, 18, 794552)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_crate_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 14, 37, 18, 792583)),
        ),
    ]
