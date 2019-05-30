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
    pjProyek = models.CharField(max_length=255, verbose_name="PJ Proyek")

    # id_user = models.ForeignKey(analis,on_delete = models.CASCADE)
    class Meta:
        db_table = 'proyek'

    def __str__(self):
        return self.nama

    def get_organisasi(self):
        return self.organisasi.all().values_list('nama_organisasi', flat=True)

    # return ', '.join(self.organisasi.all().values_list('nama_organisasi',flat=True))

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


class perangkat(models.Model):
    perangkat = JSONField()
    proyek = models.ForeignKey(proyek, on_delete=models.CASCADE, related_name='perangkat')
    penanggung_jawab = models.CharField(max_length=50, verbose_name="Nama Penanggung Jawab")

    class Meta:
        db_table = 'perangkat'

    def __str__(self):
        return self.perangkat
