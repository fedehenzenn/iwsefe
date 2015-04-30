from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from forum.models import Gamereview, Categoria, Comentario
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.


#@login_required
class review_create(CreateView):
    model = Gamereview
    fields = ['title', 'date', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        #falta agregar categoria
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


#@login_required
class review_update(UpdateView):
    model = Gamereview

    def get_success_url(self):
        return reverse('detail', kwargs={
            'pk': self.objetct.pk,
        })


#class review_detail(DetailView):
    #model = Gamereview
    #success_url = '/'

def detail_review(request, pk):
    review = Gamereview.objetct.all().filter(pk=pk)
    comentarios = Comentario.objetct.all().filter(author=review.author)
    return render(request, 'forum/gamereview_detail.html', {'review': review, 'comentarios': comentarios})


class categoria_listing(ListView):
    model = Categoria
    success_url = '/'