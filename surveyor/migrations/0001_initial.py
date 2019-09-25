# Generated by Django 2.2.1 on 2019-07-18 22:01

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projectmanajer', '0020_auto_20190718_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasil_survey', django.contrib.postgres.fields.jsonb.JSONField()),
                ('rekap_survey', models.CharField(blank=True, max_length=255)),
                ('anggota_survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anggota_survey', to='projectmanajer.anggota_survey', verbose_name='anggota_survey')),
            ],
            options={
                'db_table': 'survey',
            },
        ),
    ]
