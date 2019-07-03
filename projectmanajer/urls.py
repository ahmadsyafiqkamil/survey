from . import views
from django.urls import path

app_name = 'pm'
urlpatterns = [

    # path utama
    path('dashboard/', views.dashboardView.as_view(), name='dashboard'),
    path('buat-proyek/', views.buatproject, name='proyek'),
    path('perangkat/', views.perangkatView.as_view(), name='perangkat'),
    # path proyek
    path('list-proyek/', views.listProyek.as_view(), name='list_proyek'),
    path('detail-proyek/<int:pk>', views.detailProyek.as_view(), name='detail_proyek'),
    path('hapus-proyek/<int:pk>', views.deleteProyek.as_view(), name='hapus_proyek'),
    path('update-proyek/<int:pk>', views.updateProyek.as_view(), name='update_proyek'),
    # path organisasi
    path('detail-organisasi/<int:pk>', views.detailorganisasi.as_view(), name='detail_organisasi'),
    path('delete-organisasi/<int:pk>', views.deleteOrganisasi.as_view(), name='hapus_organisasi'),
    # path perangkat
    path('buat-perangkat', views.buat_perangkat.as_view(), name='create_perangkat'),
    path('lihat-perangkat/<int:pk>', views.lihat_perangkat.as_view(), name='view_perangkat'),
    path('delete-perangkat/<int:pk>', views.hapus_perangkat.as_view(), name='hapus_perangkat'),

]
