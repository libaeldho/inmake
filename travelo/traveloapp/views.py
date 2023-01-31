from django.shortcuts import render
from .models import Trav, Person


# Create your views here.
def tra(request):
     display1 = Trav.objects.all()
     display2 = Person.objects.all()
     return render(request, "index.html", {"Trav": display1, "Person": display2})
