from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    return render(request, 'home.html')


@staff_member_required
def restricted(request):
    return render(request, 'restricted.html', {})
