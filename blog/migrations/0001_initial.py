# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('FE', '암컷'), ('MA', '수컷')], max_length=2)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('find_point', models.CharField(max_length=200)),
                ('find_date', models.DateField(blank=True, null=True)),
                ('find_time', models.CharField(blank=True, max_length=50, null=True)),
                ('other', models.TextField()),
                ('animal_shelter', models.CharField(max_length=200)),
                ('shelter_tel', models.CharField(help_text='숫자만 10자리 입력하세요', max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('animal_move', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('고양이', '고양이'), ('강아지', '강아지')], max_length=3)),
                ('breed', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Kind'),
        ),
    ]
