from django.forms import ModelForm
from django import forms
from forum.models import *
from ckeditor.widgets import CKEditorWidget


class VotarForm (ModelForm):
    class Meta:
        model = Voto
        fields = ['valor']


class ReviewForm (ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Gamereview
        fields = ['title', 'text', 'cat']

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['text']


class DenunciaForm(ModelForm):
    class Meta:
        model = Denuncia
        fields = ['desc']