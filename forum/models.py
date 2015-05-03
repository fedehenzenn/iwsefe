from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin



# Create your models here.


class Categoria(models.Model):
    name = models.CharField(max_length=50)

<<<<<<< HEAD
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/home/categorias/'
=======
    def __str__(self):
        return self.name

    #def get_absolute_url(self):
        #return reverse("categoria", dpk=self.pk)
>>>>>>> 645e25f75bf84b03bf7ceb31c22bc8e6c4ad0f11


class Gamereview(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
<<<<<<< HEAD
    text = models.TextField()
    author = models.ForeignKey(User)
    cat = models.ForeignKey(Categoria, null=True, blank=True)
=======
    text = models.CharField(max_length=300)
    author = models.ForeignKey(User)
    cat = models.ForeignKey(Categoria, related_name="reviews")
>>>>>>> 645e25f75bf84b03bf7ceb31c22bc8e6c4ad0f11

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
        #return reverse("reviews", dpk=self.pk)


class Comentario(models.Model):
<<<<<<< HEAD
    date = models.DateTimeField()
=======
    date = models.DateTimeField(auto_now_add=True)
>>>>>>> 645e25f75bf84b03bf7ceb31c22bc8e6c4ad0f11
    author = models.ForeignKey(User)
    text = models.TextField()
    review = models.ForeignKey(Gamereview, related_name="comentarios")

<<<<<<< HEAD
    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text

=======
    class Meta:

        def __init__(self):
            ordering = ["date"]

    def __unicode__(self):
        return u"%s - %s - %s" % (self.author, self.review, self.text)
>>>>>>> 645e25f75bf84b03bf7ceb31c22bc8e6c4ad0f11
