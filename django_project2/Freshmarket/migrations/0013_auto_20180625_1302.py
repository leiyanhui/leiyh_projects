# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 05:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Freshmarket', '0012_auto_20180624_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op_name', models.CharField(max_length=254)),
                ('op_num', models.IntegerField()),
                ('op_sing_price', models.FloatField()),
                ('op_datetime', models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 13, 2, 50, 231803))),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='address',
            name='address_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 13, 2, 50, 230805)),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 25, 13, 2, 50, 230805)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 13, 2, 50, 231803)),
        ),
        migrations.AlterField(
            model_name='product_picture',
            name='picture_datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 13, 2, 50, 229808)),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_crate_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 13, 2, 50, 228811)),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scan_datatime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 13, 2, 50, 229808)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_crate_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 6, 25, 13, 2, 50, 228811)),
        ),
        migrations.AddField(
            model_name='order_products',
            name='op_foreignkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Freshmarket.Order'),
        ),
    ]
