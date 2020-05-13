from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Pet, Appointment, Owner
from django.views.generic.list import ListView






class Home(ListView):
    model = Pet

    return HttpResponse()


# Create your views here.



