from django.http import HttpResponse
from django.shortcuts import render
import datetime


def current_datetime(request):
    return render(request, "index.html")
