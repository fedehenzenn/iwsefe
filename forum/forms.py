from django.forms import ModelForm
from forum.models import Comentario
from django.contrib.auth.models import User
import datetime


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['text']

