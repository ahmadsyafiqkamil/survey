from django.contrib import admin
from .models import proyek,perangkat,organisasi,anggota_survey
# Register your models here.

admin.site.register(proyek)
admin.site.register(perangkat)
admin.site.register(anggota_survey)
admin.site.register(organisasi)
