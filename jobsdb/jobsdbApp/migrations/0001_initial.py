# Generated by Django 3.0 on 2019-12-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lowongan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jabatan', models.CharField(max_length=200)),
                ('perusahaan', models.CharField(max_length=200)),
                ('lokasi', models.CharField(max_length=200)),
                ('gaji', models.CharField(max_length=200)),
                ('deskripsi', models.TextField(max_length=200)),
                ('tanggal_publikasi', models.DateField(auto_now=True)),
                ('link_image', models.CharField(max_length=1000)),
            ],
        ),
    ]
