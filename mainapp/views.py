from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def landing_page(request):
    return HttpResponse("Hello, World")


def second_page(request):
    return HttpResponse("Hello Second")


def profile(request):
    return HttpResponse("Profile")


def count(request, angka):
    angka = angka+1
    return HttpResponse(str(angka))


def example(request):
    return render(request, 'example.html')
