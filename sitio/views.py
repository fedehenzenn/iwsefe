from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def restricted(request):
    return render(request, 'restricted.html', {})


def userprofile(request):
    return render(request, 'userprofile.html', {})