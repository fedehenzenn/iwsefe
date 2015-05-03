from django.forms import ModelForm
from forum.models import *
class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['text']

