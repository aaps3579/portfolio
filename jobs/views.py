from django.core import serializers
from django.shortcuts import render
from .models import Job
from django.http import JsonResponse


# Create your views here.

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
