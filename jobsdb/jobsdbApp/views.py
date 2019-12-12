from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
def beranda(request):
    return render(request, 'jobsdbApp/beranda.html')