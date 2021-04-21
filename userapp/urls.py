from django.urls import path, include
from . import views

app_name = 'userapp'

urlpatterns = [
    path('', views.homepage, name='Homepage')
]