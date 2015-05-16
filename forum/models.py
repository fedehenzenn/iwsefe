from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin



# Create your models here.


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
    date = models.DateTimeField()
    text = models.TextField()
    author = models.ForeignKey(User)
    cat = models.ForeignKey(Categoria, null=True, blank=True)

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
        #return reverse("reviews", dpk=self.pk)


class Comentario(models.Model):
    date = models.DateTimeField()
    author = models.ForeignKey(User)
    text = models.TextField()
    review = models.ForeignKey(Gamereview, related_name="comentarios")

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text


class Denuncia(models.Model):
    desc = models.TextField()
    date = models.DateTimeField()
    visto = models.BooleanField(default=False)
    visto_por = models.User(null=True)