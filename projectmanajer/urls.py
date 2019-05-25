from . import views
from django.urls import path

app_name = 'pm'
urlpatterns = [
	
	path('dashboard/', views.dashboardView.as_view(), name='dashboard'),
	path('buat-proyek/', views.buatproject, name='proyek'),
	path('perangkat/', views.perangkatView.as_view(), name='perangkat'),
	path('list-organisasi/', views.listOrganisasiView.as_view(), name='list_organisasi'),
	# path('detail-proyek/<int:pk>', views.detailproyek, name='detail_proyek'),
	path('detail-proyek/<int:pk>', views.detailProyek.as_view(), name='detail_proyek'),
	path('hapus-proyek/<int:pk>', views.deleteProyek.as_view(), name='hapus_proyek'),
	# path('detail-proyek/<int:pk>', views.detailProyeka, name='detail_proyek'),
]
