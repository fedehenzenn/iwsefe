from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.


class Categoria(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse2("categoria", dpk=self.pk)


class Gamereview(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    text = models.CharField(max_length=300)
    author = models.ForeignKey(User)
    cat = models.ForeignKey(Categoria, related_name="reviews")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse2("reviews", dpk=self.pk)


class Commentario(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    text = models.TextField()
    review = models.ForeignKey(Gamereview, related_name="comentarios")

    class Meta:

        def __init__(self):
            ordering = ["created"]

    def __unicode__(self):
        return u"%s - %s - %s" % (self.author, self.review, self.text

