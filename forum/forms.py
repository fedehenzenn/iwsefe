from django.forms import ModelForm
from forum.models import *
from shared.utils import ContainerFormMixin


class ComentarioForm(ContainerFormMixin, ModelForm):
    class Meta:
        model = ComentarioPost
        exclude = ["author", "review"]