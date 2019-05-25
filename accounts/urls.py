from . import views
from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    path('',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout, name='logout'),
]
