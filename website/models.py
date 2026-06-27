from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# Model untuk Buku (Gabungkan semua field di sini)
class Buku(models.Model):
    KATEGORI_CHOICES = [
        ('fiksi', 'Fiksi'),
        ('nonfiksi', 'Non-Fiksi'),
    ]
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='buku/')
    # PASTIKAN BARIS INI ADA:
    kategori = models.CharField(max_length=10, choices=KATEGORI_CHOICES, default='fiksi') 
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.judul

# Model untuk Agenda
class Agenda(models.Model):
    nama_agenda = models.CharField(max_length=200)
    tanggal = models.DateField()
    # GANTI upload_image JADI upload_to
    gambar = models.ImageField(upload_to='agenda/')
    deskripsi = models.TextField()

    def clean(self):
        super().clean()
        if self.tanggal and self.tanggal < timezone.localdate():
            raise ValidationError({
                'tanggal': 'Tanggal agenda tidak boleh lebih awal dari hari ini.'
            })

    def __str__(self):
        return self.nama_agenda

# Model untuk Dokumentasi
class Dokumentasi(models.Model):
    keterangan = models.CharField(max_length=200)
    # GANTI upload_image JADI upload_to
    gambar = models.ImageField(upload_to='dokumentasi/')
    tanggal_kegiatan = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.keterangan
