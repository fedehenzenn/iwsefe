from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from forum.models import *
from forum.forms import *
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
import datetime


class LoginRequieredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequieredMixin, cls).as_view(**initkwargs)
        return login_required(view)

# Create your views here.


#@login_required
class review_create(LoginRequieredMixin, CreateView):
    model = Gamereview
    fields = ['title', 'date', 'text', 'cat']
    model.estado = "Publicado"
    template_name = 'forum/gamereview_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(review_create, self).form_valid(form)

    def get_success_url(self):
        return '/home'


#@login_required
class review_delete(LoginRequieredMixin, DeleteView):
    model = Gamereview
    success_url = '/home'


class review_listing(ListView):
    model = Gamereview
    success_url = '/home'


#@login_required
class review_update(LoginRequieredMixin, UpdateView):
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
    reviews = Gamereview.objects.all()
    return render(request, 'forum/categoria_list.html', {'categorias': categorias, 'reviews' : reviews})


@login_required
def comentar(request, pk):
    review = Gamereview.objects.all().filter(pk=pk)[0]
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


class categoria_add(LoginRequieredMixin, CreateView):
    model = Categoria
    fields = ['name']
    template_name ='forum/categoria_add.html'

@login_required
def denunciar(request, pk):
    review = Gamereview.objects.all().filter(pk=pk)[0]
    if request.method == 'POST':
        # formulario enviado
        denuncia_form = DenunciaForm(request.POST)

        if denuncia_form.is_valid():
            # formulario validado correctamente
            denuncia_form.instance.date = datetime.datetime.now()
            denuncia_form.instance.visto_por = request.user
            denuncia_form.instance.review = review
            denuncia_form.save()

            return HttpResponseRedirect(reverse('detail',args=[review.pk]))

    else:
        # formulario inicial
        denuncia_form = DenunciaForm(instance=request.user)

    return render_to_response('forum/denuncia_form.html', { 'denuncia_form': denuncia_form },
        context_instance=RequestContext(request))
