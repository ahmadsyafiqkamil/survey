from . import views
from django.urls import path, include

app_name = 'surveyor'
urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),

]
