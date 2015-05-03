from django.forms import ModelForm
from forum.models import *
<<<<<<< HEAD


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['text']
=======
from shared.utils import ContainerFormMixin


class ComentarioForm(ContainerFormMixin, ModelForm):
    class Meta:
        model = ComentarioPost
        exclude = ["author", "review"]
>>>>>>> 645e25f75bf84b03bf7ceb31c22bc8e6c4ad0f11
