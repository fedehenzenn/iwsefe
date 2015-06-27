from django.shortcuts import render
from forum.models import Gamereview


def home(request):
    reviews = Gamereview.objects.all()
    return render(request, 'home.html', {'reviews': reviews})

def cat_error(request):
    return render(request, 'cat_error.html', {})


def restricted(request):
    return render(request, 'restricted.html', {})


def userprofile(request):
    return render(request, 'userprofile.html', {})