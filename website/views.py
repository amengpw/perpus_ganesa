from django.shortcuts import render, get_object_or_404
from .models import Buku, Agenda

def index(request):
    agenda_list = Agenda.objects.all()
    return render(request, 'index.html', {'agenda_list': agenda_list})

def search_buku(request):
    query = request.GET.get('q')
    hasil_buku = []
    rekomendasi = None
    
    if query:
        hasil_buku = Buku.objects.filter(judul__icontains=query)
    
    if not hasil_buku:
        rekomendasi = Buku.objects.all().order_by('?')[:3]
        
    return render(request, 'search_results.html', {
        'hasil_buku': hasil_buku,
        'query': query,
        'rekomendasi': rekomendasi
    })

def detail_buku(request, id):
    buku = get_object_or_404(Buku, id=id)
    return render(request, 'detail_buku.html', {'buku': buku})

def profil(request):
    return render(request, 'profil.html')

def staff(request):
    return render(request, 'staff.html')