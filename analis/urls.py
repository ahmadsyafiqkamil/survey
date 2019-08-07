from django.urls import path
from . import views

app_name = 'analis'
urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('list-project/',views.list_project.as_view(), name='list_project'),
    path('list-organisasi/<int:pk_proyek>',views.list_organisasi.as_view(), name='list_organisasi'),
    path('hasil-survey/<int:pk_anggota_survey>',views.hasil_survey.as_view(), name='hasil_survey'),
    path('rekap-survey/',views.rekap_survey.as_view(), name='rekap_survey'),

    

    ]
