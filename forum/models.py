from django.db import models
8
# Create your models here.


class post(models.Model):
    titulo = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    texto = models.CharField(max_length=300)

    def __str__(self):
        return self.titulo
