from django.urls import path
from . import views

app_name = 'analis'
urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    
    

    ]
