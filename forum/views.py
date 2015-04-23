from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, DetailView, ListView,UpdateView
from forum.models import Gamereview
from django.core.url.urlresolver import reverse

# Create your views here.

@login_required
class review_create(CreateView):
    model = Gamereview

@login_required
class review_delete(DeleteView):
    model = Gamereview
    success_url = '/'


class review_listing(ListView):
    model = Gamereview


