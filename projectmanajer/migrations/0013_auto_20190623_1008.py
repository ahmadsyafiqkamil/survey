# Generated by Django 2.2.1 on 2019-06-23 10:08

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanajer', '0012_auto_20190623_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perangkat',
            name='perangkat',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]