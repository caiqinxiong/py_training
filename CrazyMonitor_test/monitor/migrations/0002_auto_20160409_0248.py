# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-09 02:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TriggerExpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u89e6\u53d1\u5668\u8868\u8fbe\u5f0f\u540d\u79f0')),
                ('logic_type', models.CharField(blank=True, choices=[(b'or', b'OR'), (b'and', b'AND')], max_length=32, null=True, verbose_name='\u903b\u8f91\u5173\u7cfb')),
                ('operator_type', models.CharField(choices=[(b'eq', b'='), (b'lt', b'<'), (b'gt', b'>')], max_length=32, verbose_name='\u8fd0\u7b97\u7b26')),
                ('threshold', models.IntegerField(verbose_name='\u9608\u503c')),
                ('left_sibling', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='left_sibling_condition', to='monitor.TriggerExpression', verbose_name='\u5de6\u8fb9\u6743\u9650')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Service', verbose_name='\u5173\u8054\u670d\u52a1')),
                ('service_index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.ServiceIndex', verbose_name='\u5173\u8054\u670d\u52a1\u6307\u6807')),
            ],
        ),
        migrations.RemoveField(
            model_name='trigger',
            name='expression',
        ),
        migrations.AddField(
            model_name='trigger',
            name='expressions',
            field=models.ManyToManyField(to='monitor.TriggerExpression', verbose_name='\u6761\u4ef6\u8868\u8fbe\u5f0f'),
        ),
    ]
