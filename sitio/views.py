from django.shortcuts import render
from forum.models import Gamereview


def home(request):
    reviews = Gamereview.objects.all()
    return render(request, 'home.html', {'reviews': reviews})


def restricted(request):
    return render(request, 'restricted.html', {})


def userprofile(request):
    return render(request, 'userprofile.html', {})