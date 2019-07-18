from . import views
from django.urls import path, include

app_name = 'surveyor'
urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('list-project/',views.list_project.as_view(), name='list_project'),
    path('survey-organisasi/<int:pk>',views.survey_organisasi.as_view(), name='survey_organisasi'),

]
