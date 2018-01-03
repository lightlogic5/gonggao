# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-03 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='articale',
            name='a_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gongg.project'),
        ),
        migrations.AddField(
            model_name='articale',
            name='a_tag',
            field=models.ManyToManyField(blank=True, null=True, to='gongg.tags', verbose_name='选择文章标签'),
        ),
    ]