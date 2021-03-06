# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 19:40
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='atributi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atributi', models.CharField(max_length=250)),
                ('vlera', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='biznes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biznes', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('kryesore', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='lloji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lloji', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='prona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmimi', models.IntegerField()),
                ('dhoma', models.IntegerField()),
                ('banjo', models.IntegerField()),
                ('size', models.IntegerField()),
                ('titulli', models.CharField(max_length=250)),
                ('pershkrim', models.CharField(max_length=1000)),
                ('status', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('url', models.CharField(max_length=100)),
                ('hits', models.IntegerField()),
                ('creation_date', models.DateField(default=datetime.datetime.now)),
                ('modif_date', models.DateField(default=datetime.datetime.now)),
                ('sponsorizuar', models.IntegerField()),
                ('id_biznes', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.biznes')),
                ('id_lloji', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.lloji')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='qytet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qytet', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='rruget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emri', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='vendodhje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_rruga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.rruget')),
            ],
        ),
        migrations.CreateModel(
            name='zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(max_length=250)),
                ('id_qytet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.qytet')),
            ],
        ),
        migrations.AddField(
            model_name='vendodhje',
            name='id_zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.zona'),
        ),
        migrations.AddField(
            model_name='prona',
            name='id_vendodhje',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.vendodhje'),
        ),
        migrations.AddField(
            model_name='foto',
            name='id_prona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.prona'),
        ),
        migrations.AddField(
            model_name='atributi',
            name='id_prona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.prona'),
        ),
    ]
