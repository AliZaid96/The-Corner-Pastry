

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('index-admin/', views.index_admin, name='index_admin'),
]
