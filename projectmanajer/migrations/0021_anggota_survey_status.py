# Generated by Django 2.2.1 on 2019-07-25 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanajer', '0020_auto_20190718_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='anggota_survey',
            name='status',
            field=models.CharField(choices=[(1, 'Sudah Melakukan Survey'), (0, 'Belum Melakukan Survey')], default=0, max_length=2),
        ),
    ]
