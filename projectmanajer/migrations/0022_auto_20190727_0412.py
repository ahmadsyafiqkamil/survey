# Generated by Django 2.2.1 on 2019-07-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanajer', '0021_anggota_survey_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anggota_survey',
            name='status',
            field=models.IntegerField(choices=[(1, 'Sudah Melakukan Survey'), (0, 'Belum Melakukan Survey')], default=0, max_length=2),
        ),
    ]
