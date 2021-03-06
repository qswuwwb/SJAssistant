# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 08:04
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
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='访谈时间')),
                ('operator', models.CharField(choices=[('YinSJ', '尹胜杰'), ('GuoQH', '郭巧会'), ('JinNa', '金娜')], max_length=10, verbose_name='访谈人')),
                ('deportment_score', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='仪态')),
                ('deportment_problem', models.CharField(blank=True, default='', max_length=50, verbose_name='存在的问题')),
                ('expression_score', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='表达')),
                ('expression_problem', models.CharField(blank=True, default='', max_length=50, verbose_name='存在的问题')),
                ('resume_score', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='简历')),
                ('resume_problem', models.CharField(blank=True, default='', max_length=50, verbose_name='存在的问题')),
                ('background_score', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='背景')),
                ('background_problem', models.CharField(blank=True, default='', max_length=50, verbose_name='存在的问题')),
                ('project_score', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='项目')),
                ('project_problem', models.CharField(blank=True, default='', max_length=50, verbose_name='存在的问题')),
                ('skill_point_score', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='技能')),
                ('skill_point_problem', models.CharField(blank=True, default='', max_length=50, verbose_name='存在的问题')),
                ('mentality_score', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='心态')),
                ('mentality_problem', models.CharField(blank=True, default='', max_length=50, verbose_name='存在的问题')),
                ('task', models.TextField(verbose_name='要求')),
                ('task_completion', models.TextField(blank=True, default='', verbose_name='评语')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentBasic.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name_plural': '访谈',
                'verbose_name': '访谈',
            },
        ),
    ]
