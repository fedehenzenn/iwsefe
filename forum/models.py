from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Categoria(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/home/categorias/'


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

