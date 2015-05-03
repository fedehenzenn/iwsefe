<<<<<<< HEAD
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
=======
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from forum.models import Gamereview, Categoria, Comentario
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
>>>>>>> 645e25f75bf84b03bf7ceb31c22bc8e6c4ad0f11


# Create your views here.


#@login_required
class review_create(CreateView):
    model = Gamereview
<<<<<<< HEAD
    fields = ['title', 'date', 'text', 'cat']
    template_name ='forum/gamereview_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(review_create, self).form_valid(form)

    def get_success_url(self):
        return '/home'
=======
    fields = ['title', 'date', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        #falta agregar categoria
        return super(review_create, self).form_valid(form)

    def get_success_url(self):
        return '/'
>>>>>>> 645e25f75bf84b03bf7ceb31c22bc8e6c4ad0f11


#@login_required
class review_delete(DeleteView):
    model = Gamereview
    success_url = '/home'


class review_listing(ListView):
    model = Gamereview
    success_url = '/home'


<<<<<<< HEAD
=======

>>>>>>> 645e25f75bf84b03bf7ceb31c22bc8e6c4ad0f11
#@login_required
class review_update(UpdateView):
    model = Gamereview

    def get_success_url(self):
        return reverse('detail', kwargs={
            'pk': self.objects.pk,
        })


<<<<<<< HEAD
def detail_review(request, pk):
    review = Gamereview.objects.all().filter(pk=pk)
    comentarios = Comentario.objects.exclude(author__isnull=True)
    return render(request, 'forum/gamereview_detail.html', {'review': review, 'comentarios': comentarios, 'pk' : pk})

def categorias_listing(request):
    categorias = Categoria.objects.all()
    return render(request, 'forum/categoria_list.html', { 'categorias': categorias })


@login_required
def comentar(request, pk):
    review = Gamereview.objects.all().filter(pk=pk)
    comentarios = Comentario.objects.exclude(author__isnull=True)
    if request.method == 'post':
        # formulario enviado
        cometario_form = ComentarioForm(request.post)

        if comentario_form.is_valid():
            # formulario validado correctamente
            cometario_form.instance.date = datetime.datetime.now()
            cometario_form.instance.author = request.user
            cometario_form.instance.review = review
            cometario_form.save()

            return HttpResponseRedirect('forum/gamereview_detail.html', {'review': review, 'comentarios': comentarios})

    else:
        # formulario inicial
        cometario_form = ComentarioForm(instance=request.user)

    return render_to_response('forum/gamereview_post.html', { 'cometario_form': cometario_form },
        context_instance=RequestContext(request))


class categoria_add(CreateView):
    model = Categoria
    fields = ['name']
    template_name ='forum/categoria_add.html'
=======
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
>>>>>>> 645e25f75bf84b03bf7ceb31c22bc8e6c4ad0f11
