# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('StudentBasic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('overtime_day', '加班一天'), ('overtime_night', '加班一晚'), ('overtime_onduty', '夜晚值班'), ('leave', '请假一天')], max_length=20, null=True, verbose_name='加班/请假类型')),
                ('date', models.DateField(null=True, unique=True, verbose_name='日期')),
                ('reason', models.CharField(max_length=50, null=True, verbose_name='加班原因')),
                ('assistant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='StudentBasic.Assistant', verbose_name='项目经理')),
            ],
            options={
                'verbose_name_plural': '加班与请假',
                'verbose_name': '加班与请假',
            },
        ),
    ]
