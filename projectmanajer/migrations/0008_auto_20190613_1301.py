# Generated by Django 2.2.1 on 2019-06-13 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanajer', '0007_auto_20190613_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perangkat',
            name='proyek',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perangkat', to='projectmanajer.proyek'),
        ),
    ]