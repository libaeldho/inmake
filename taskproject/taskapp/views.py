from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return HttpResponse("we are here for you since 2006")


def details(request):
    return render(request, "details.html")


def contact(request):
    return HttpResponse("contact in facebook @ammoos opticals")


def thanks(request):
    return render(request, "thanks.html")
