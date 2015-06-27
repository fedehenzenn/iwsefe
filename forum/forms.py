from django.forms import ModelForm
from forum.models import Comentario, Denuncia, Gamereview
from suit_redactor.widgets import RedactorWidget


class ReviewForm (ModelForm):
    class Meta:
        model = Gamereview
        fields = ['title', 'text']
        widgets = {
            'text': RedactorWidget(editor_options={'lang': 'es'})
        }


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['text']


class DenunciaForm(ModelForm):
    class Meta:
        model = Denuncia
        fields = ['desc']