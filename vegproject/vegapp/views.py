from django.shortcuts import render

from .models import vege


# Create your views here.
def veg(request):
    veg = vege.objects.all()
    return render(request, "index.html", )
