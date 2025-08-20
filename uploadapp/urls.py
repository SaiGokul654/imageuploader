# uploadapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),   # adjust view name
    path('gallery/', views.gallery, name='gallery'),
]
