from django.shortcuts import render

from .models import Trav, Person


# Create your views here.
def tra(request):
    tra = Trav.objects.all()
    return render(request, "index.html", {'result': tra})


def tour(request):
    tour = Person.objects.all()
    return render(request, "index.html", {'result': tour})
