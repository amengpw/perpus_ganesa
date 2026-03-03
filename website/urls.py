from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_buku, name='search_buku'),
    path('buku/<int:id>/', views.detail_buku, name='detail_buku'),
    path('profil/', views.profil, name='profil'),
    path('staff/', views.staff, name='staff'),
    path('peminjaman/', views.peminjaman, name='peminjaman'),
    path('tutorial_member/', views.tutorial_member, name='tutorial_member'),

]