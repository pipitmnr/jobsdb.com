from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
def beranda(request):
    return render(request, 'jobsdbApp/beranda.html')
def searchResult(request):
    return render(request, 'jobsdbApp/search-result.html')
def detailLowongan(request):
    return render(request, 'jobsdbApp/detail-lowongan.html')