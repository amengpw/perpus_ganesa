from django.shortcuts import render, get_object_or_404
from .models import Buku, Agenda, Dokumentasi
from django.utils import timezone

def index(request):
    # Ambil 5 buku fiksi & 5 non-fiksi untuk section Top Rekomendasi
    buku_fiksi = Buku.objects.filter(kategori='fiksi')[:5]
    buku_nonfiksi = Buku.objects.filter(kategori='nonfiksi')[:5]
    
    # Ambil semua data agenda & dokumentasi
    hari_ini = timezone.now().date()
    
    # Filter agenda yang tanggalnya HARI INI atau DI MASA DEPAN
    # Diurutkan berdasarkan tanggal yang paling dekat ('tanggal' tanpa minus)
    # Lalu batasi hanya tampil 3 agenda saja
    list_agenda = Agenda.objects.filter(tanggal__gte=hari_ini).order_by('tanggal')[:3]
    galeri = Dokumentasi.objects.all()

    context = {
        'buku_fiksi': buku_fiksi,
        'buku_nonfiksi': buku_nonfiksi,
        'list_agenda': list_agenda,
        'galeri': galeri,
    }
    return render(request, 'index.html', context)

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

def denah(request):
    return render(request, 'denah.html')

def staff(request):
    return render(request, 'staff.html')

def peminjaman(request):
    return render(request, 'peminjaman.html')

def tutorial_member(request):
    return render(request, 'tutorial_member.html')

def tata_tertib(request):
    return render(request, 'tata_tertib.html')

def fasilitas(request):
    return render(request, 'fasilitas.html')

def agenda(request):
    # Menarik semua agenda, diurutkan dari yang terbaru (-tanggal)
    agenda_lengkap = Event.objects.all().order_by('-tanggal')
    
    context = {
        'agenda': agenda_lengkap
    }
    return render(request, 'agenda.html', context)