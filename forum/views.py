from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from forum.models import *
from forum.forms import *
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
import datetime



# Create your views here.


#@login_required
class review_create(CreateView):
    model = Gamereview
    fields = ['title', 'date', 'text', 'cat']
    template_name ='forum/gamereview_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(review_create, self).form_valid(form)

    def get_success_url(self):
        return '/home'


#@login_required
class review_delete(DeleteView):
    model = Gamereview
    success_url = '/home'


class review_listing(ListView):
    model = Gamereview
    success_url = '/home'


#@login_required
class review_update(UpdateView):
    model = Gamereview

    def get_success_url(self):
        return reverse('detail', kwargs={
            'pk': self.objects.pk,
        })


def detail_review(request, pk):
    review = Gamereview.objects.all().filter(pk=pk)[0]
    comentarios = Comentario.objects.exclude(author__isnull=True)
    return render(request, 'forum/gamereview_detail.html', {'review': review, 'comentarios': comentarios, 'pk' : pk})

def categorias_listing(request):
    categorias = Categoria.objects.all()
    return render(request, 'forum/categoria_list.html', { 'categorias': categorias })


@login_required
def comentar(request, pk):
    review = Gamereview.objects.all().filter(pk=pk)[0]
    comentarios = Comentario.objects.exclude(author__isnull=True)
    if request.method == 'POST':
        # formulario enviado
        comentario_form = ComentarioForm(request.POST)

        if comentario_form.is_valid():
            # formulario validado correctamente
            comentario_form.instance.date = datetime.datetime.now()
            comentario_form.instance.author = request.user
            comentario_form.instance.review = review
            comentario_form.save()

            return HttpResponseRedirect(reverse('detail',args=[review.pk]))

    else:
        # formulario inicial
        comentario_form = ComentarioForm(instance=request.user)

    return render_to_response('forum/gamereview_post.html', { 'comentario_form': comentario_form },
        context_instance=RequestContext(request))


class categoria_add(CreateView):
    model = Categoria
    fields = ['name']
    template_name ='forum/categoria_add.html'

