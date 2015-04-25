from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forum.models import Gamereview


def home(request):
    return render(request, 'home.html')


@login_required
def restricted(request):
    return render(request, 'restricted.html', {})
