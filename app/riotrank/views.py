from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def riotrank(request):
    return render(request, "riotrank.html")
