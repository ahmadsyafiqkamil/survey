from django.db import models

# Create your models here.

from django.db import models
from django.contrib.postgres.fields import JSONField
from accounts.models import User

# Create your models here.
class proyek(models.Model):
    nama = models.CharField(max_length=255, verbose_name="Nama Proyek")
    deskripsi = models.TextField(verbose_name="Deskripsi Proyek");
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pjProyek = models.CharField(max_length=255, verbose_name="Penanggung Jawav Proyek")

    # id_user = models.ForeignKey(analis,on_delete = models.CASCADE)

    class Meta:
        db_table = 'proyek'

    def __str__(self):
        return self.nama

    def get_organisasi(self):
        return self.organisasi.all().values_list('nama_organisasi', flat=True)

    def get_pj_organisasi(self):
        return self.organisasi.all().values_list('narasumber', flat=True)

    def get_perangkat(self):
        return self.perangkat.all().values_list('perangkat', flat=True)

    def get_narasumber_perangkat(self):
        return self.perangkat.all().values_list('penanggung_jawab', flat=True)


class organisasi(models.Model):
    nama_organisasi = models.CharField(max_length=255, blank=True)
    narasumber = models.CharField(max_length=50, verbose_name="Narasumber", blank=True, null=True)
    proyek = models.ForeignKey(proyek, related_name='organisasi', on_delete=models.CASCADE)

    class Meta:
        db_table = 'organisasi'

    def __str__(self):
        return self.nama_organisasi

    def get_proyek_id(self):
        return proyek.pk

    # def get_surveyor(self):
    #     return self.

class perangkat(models.Model):
    nama_perangkat = models.CharField(max_length=255, blank=True)
    perangkat = JSONField()
    proyek = models.OneToOneField(proyek, on_delete=models.CASCADE, related_name='perangkat')
    penanggung_jawab = models.CharField(max_length=50, verbose_name="Nama Penanggung Jawab")

    class Meta:
        db_table = 'perangkat'

    def __str__(self):
        return self.nama_perangkat

    def get_proyek(self):
        return self.proyek.nama


class anggota_survey(models.Model):
    PILIHAN_STATUS = [
        (1,'Sudah Melakukan Survey'),
        (0,'Belum Melakukan Survey'),

    ]
    anggota = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User', verbose_name='Surveyor')
    survey_organisasi = models.ForeignKey(organisasi, on_delete=models.CASCADE, related_name='organisasi',
                                          verbose_name='Organisasi')
    status = models.IntegerField(choices=PILIHAN_STATUS, default=0)

    class Meta:
        db_table = 'anggota_survey'

    def __str__(self):
        return self.survey_organisasi.nama_organisasi
        # return self.survey_organisasi

    def get_user_name(self):
        return self.anggota.user_name

    def get_organisasi_name(self):
        return self.survey_organisasi

    def get_project(self):
        return self.survey_organisasi.proyek

    def get_id_project(self):
        return self.survey_organisasi.proyek_id

    def get_id(self):
        return self.pk


class analis_proyek(models.Model):
    proyek = models.ForeignKey(proyek,on_delete=models.CASCADE, related_name='proyek', verbose_name='Proyek')
    analis = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Analis')

    class Meta:
        db_table = 'analis_proyek'

    def __str__(self):
        return self.analis.user_name


