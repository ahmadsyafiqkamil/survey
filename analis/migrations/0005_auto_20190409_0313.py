# Generated by Django 2.1.7 on 2019-04-09 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analis', '0004_auto_20190409_0312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisasi',
            old_name='id_proyek',
            new_name='proyek',
        ),
    ]
