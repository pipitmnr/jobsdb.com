from django.db import models

# Create your models here.
class Lowongan(models.Model):
    jabatan = models.CharField(max_length=200)
    lokasi = models.CharField(max_length=200)
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField(max_length=200)
    perusahaan = models.CharField(max_length=200)
    tanggal_publikasi = models.DateField(auto_now=True)

class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    tanggal_publikasi = models.DateField(auto_now=True)
    thumbnail = models.CharField(max_length=200)
    isi = models.TextField(max_length=10000)
