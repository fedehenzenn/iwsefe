from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Gamereview(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    text = models.CharField(max_length=300)
    author = models.ForeignKey(User)
    cat = models.ForeignKey(Categoria, null=True, blank=True)

    def __str__(self):
        return self.title

