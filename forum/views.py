from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from forum.models import Gamereview
from django.core.urlresolvers import reverse
from django.utils.functional import lazy

# Create your views here.

#@login_required
class review_create(CreateView):
    model = Gamereview
    fields = ['title', 'date', 'text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(review_create, self).form_valid(form)

    def get_success_url(self):
        return '/'


#@login_required
class review_delete(DeleteView):
    model = Gamereview
    success_url = '/'


class review_listing(ListView):
    model = Gamereview
    success_url = '/'

class review_update(UpdateView):
    model = Gamereview

    def get_success_url(self):
        return reverse('detail', kwargs={
            'pk': self.objetct.pk,
        })


class review_detail(DetailView):
    model = Gamereview
    success_url = '/'