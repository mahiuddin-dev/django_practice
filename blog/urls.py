from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name='Homepage'),
    path("blogpost/<int:post_id>", views.blogpost, name='Blogpost')
]