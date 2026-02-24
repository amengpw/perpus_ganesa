from django.db import models

class Buku(models.Model):  # Pastikan 'B' kapital
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='buku/')
    deskripsi = models.TextField()

    def __str__(self):
        return self.judul

class Agenda(models.Model):  # Pastikan 'A' kapital
    judul = models.CharField(max_length=200)
    tanggal = models.DateField()
    foto = models.ImageField(upload_to='agenda/')

    def __str__(self):
        return self.judul
