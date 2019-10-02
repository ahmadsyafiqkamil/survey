from django.db import models
from accounts.models import User
from projectmanajer.models import perangkat, proyek, organisasi, anggota_survey
from accounts.models import User
from django.contrib.postgres.fields import JSONField


class survey(models.Model):
    hasil_survey = JSONField()
    anggota_survey = models.ForeignKey(anggota_survey, on_delete=models.CASCADE, related_name='anggota_survey',
                                       verbose_name='Organisasi')

    class Meta:
        db_table = 'survey'

    def __str__(self):
        return self.get_organisasi_name()

    def get_proyek_id(self):
        return self.anggota_survey.survey_organisasi.organisasi.proyek.pk

    def get_organisasi_name(self):
        return self.anggota_survey.survey_organisasi.nama_organisasi

    def get_proyek_name(self):
        return self.anggota_survey.survey_organisasi.proyek.nama

    def get_survey(self):
        return self.anggota_survey.survey_organisasi.proyek.perangkat.perangkat

    def get_anggota_survey(self):
        return self.anggota_survey_id


class lampiran(models.Model):
    file = models.FileField(upload_to='attachments')
    survey = models.OneToOneField(survey, on_delete=models.CASCADE)
