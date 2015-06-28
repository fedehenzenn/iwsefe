from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from datetime import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
today = datetime.now()

# Create your models here.h


class Categoria(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/home/categorias/'

    #def get_absolute_url(self):
        #return reverse("categoria", dpk=self.pk)



class Gamereview(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    text = RichTextField()
    estado = models.CharField(max_length=50)
    author = models.ForeignKey(User)
    cat = models.ForeignKey(Categoria, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('detail', args=[self.pk])


class Comentario(models.Model):
    date = models.DateTimeField()
    author = models.ForeignKey(User)
    text = models.TextField()
    review = models.ForeignKey(Gamereview, related_name="comentarios")

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('detail', args=[self.review.pk])


class Denuncia(models.Model):
    desc = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    visto = models.BooleanField(default=False)
    visto_por = models.ForeignKey(User, null=True)
    review = models.ForeignKey(Gamereview, null=True)

    def __unicode__(self):
        return self.desc

    def __str__(self):
        return self.desc




class IntegerRangeField(models.IntegerField):


    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Voto (models.Model):
    author = models.ForeignKey(User)
    review = models.ForeignKey(Gamereview)
    valor = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

