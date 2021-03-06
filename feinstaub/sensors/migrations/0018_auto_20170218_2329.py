# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0017_auto_20160416_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='pin',
            field=models.CharField(db_index=True, default='-', help_text='differentiate the sensors on one node by giving pin used', max_length=10),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='public',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='timestamp',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sensordatavalue',
            name='value_type',
            field=models.CharField(choices=[('P1', '1µm particles'), ('P2', '2.5µm particles'), ('durP1', 'duration 1µm'), ('durP2', 'duration 2.5µm'), ('ratioP1', 'ratio 1µm in percent'), ('ratioP2', 'ratio 2.5µm in percent'), ('samples', 'samples'), ('min_micro', 'min_micro'), ('max_micro', 'max_micro'), ('temperature', 'Temperature'), ('humidity', 'Humidity'), ('pressure', 'Pa'), ('altitude', 'meter'), ('pressure_sealevel', 'Pa (sealevel)'), ('brightness', 'Brightness'), ('dust_density', 'Dust density in mg/m3'), ('vo_raw', 'Dust voltage raw'), ('voltage', 'Dust voltage calculated'), ('P10', '1µm particles'), ('P25', '2.5µm particles'), ('durP10', 'duration 1µm'), ('durP25', 'duration 2.5µm'), ('ratioP10', 'ratio 1µm in percent'), ('ratioP25', 'ratio 2.5µm in percent'), ('door_state', 'door state (open/closed)'), ('lat', 'latitude'), ('lon', 'longitude'), ('height', 'height'), ('hdop', 'horizontal dilusion of precision'), ('timestamp', 'measured timestamp'), ('age', 'measured age'), ('satelites', 'number of satelites'), ('speed', 'current speed over ground'), ('azimuth', 'track angle')], db_index=True, max_length=100),
        ),
        migrations.AlterIndexTogether(
            name='sensordata',
            index_together=set([('modified',)]),
        ),
    ]
