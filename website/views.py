from django.shortcuts import render
from .models import Buku, Agenda  # Harus sama persis dengan yang di models.py

def index(request):
    data_buku = Buku.objects.all()
    data_agenda = Agenda.objects.all()
    return render(request, 'index.html', {
        'katalog': data_buku, 
        'agenda': data_agenda
    })
