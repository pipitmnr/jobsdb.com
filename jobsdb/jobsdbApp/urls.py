from django.urls import path
from . import views


urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('event/', views.event, name='event'),
    path('artikel/<artikel_id>', views.artikel, name='artikel'),
    path('artikel', views.resource, name='resource')
]