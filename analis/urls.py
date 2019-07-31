from django.urls import path
from . import views

app_name = 'analis'
urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('list-project/',views.list_project.as_view(), name='list_project'),
    path('rekap-survey/',views.rekap_survey.as_view(), name='rekap_survey'),

    

    ]
