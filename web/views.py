from django.shortcuts import render
from django.http import HttpResponse

from .models import Screening


def index(request):
    return render(request, 'index.html')


def status(request):
    return HttpResponse('Hello from Python!')


def db(request):
    screenings = Screening.objects.all()
    return render(request, 'db.html', {'screenings': screenings})
