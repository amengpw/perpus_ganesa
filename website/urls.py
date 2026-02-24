from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_buku, name='search_buku'),
    path('buku/<int:id>/', views.detail_buku, name='detail_buku'),
]