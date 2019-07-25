from django.db import models
from accounts.models import User
from projectmanajer.models import perangkat,proyek,organisasi,anggota_survey
from accounts.models import User
from django.contrib.postgres.fields import JSONField

class survey(models.Model):
    hasil_survey = JSONField()
    # rekap_survey = models.CharField(max_length=255, blank=True)
    anggota_survey = models.ForeignKey(anggota_survey,on_delete=models.CASCADE, related_name='anggota_survey', verbose_name='anggota_survey')
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'survey'





