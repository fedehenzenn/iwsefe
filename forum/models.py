from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Gamereview(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    text = models.CharField(max_length=300)
#    author = models.ForeingKey(User)

    def __str__(self):
        return self.title
