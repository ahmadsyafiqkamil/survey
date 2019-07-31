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
    path('tambah-organisasi/<int:pk>', views.tambahOrganisasi.as_view(), name='tambah_organisasi'),
    # path perangkat
    path('buat-perangkat', views.buat_perangkat.as_view(), name='create_perangkat'),
    path('lihat-perangkat/<int:pk>', views.lihat_perangkat.as_view(), name='view_perangkat'),
    path('delete-perangkat/<int:pk>', views.hapus_perangkat.as_view(), name='hapus_perangkat'),
    path('update-perangkat/<int:pk>', views.update_perangkat.as_view(), name='update_perangkat'),
    #    path member
    path('manajemen-member/', views.manajemen_member.as_view(), name='manajemen_member'),
    path('detail-member/<int:pk>', views.detail_member.as_view(), name='detail_member'),
    path('hapus-member/<int:pk>', views.hapus_member.as_view(), name='hapus_member'),
    path('plot-surveyor/<int:pk>', views.plot_surveyor.as_view(), name='plot_surveyor'),
    path('detail-organisasi-surveyor/<int:pk>', views.detail_organisasi_surveyor.as_view(),
         name='detail_organisasi_surveyor'),
    path('hapus-organisasi-surveyor/<int:pk>', views.hapus_organisasi_surveyor.as_view(),
         name='hapus_organisasi_surveyor'),
    # analis
    path('plot-analis/<int:pk>', views.plot_analis.as_view(),name='plot_analis'),
    path('detail-analis-surveyor/<int:pk>', views.detail_analis_surveyor.as_view(),name='detail_analis_survey'),
    path('delete-analis-surveyor/<int:pk>', views.delete_analis_surveyor.as_view(),name='delete_analis_survey'),

]
