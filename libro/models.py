from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime

# Create your models here.

@python_2_unicode_compatible # only if you need to support Python 2
class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(datetime.datetime.now())

    def __str__(self): return self.nombre
