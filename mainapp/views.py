from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def landing_page(request):
    return HttpResponse("Hello, World!")


def second_page(request):
    return HttpResponse("SecondPage")


def profile(request):
    return HttpResponse("profile ku")


def count(request, angka):
    angka = angka+1
    return HttpResponse(str(angka))


def sapa(request, nama):
    return HttpResponse("Halo "+nama)


def example(request):
    return render(request, 'example.html')


def newpage(request):
    return HttpResponse("new")


def a(request):
    return HttpResponse()


def resume_nova(request):
    return render(request, 'resume-nova.html')


def toko_nova(request):
    return render(request, 'toko-nova.html')
