from django.db import models

# Create your models here.

class Desagregacion(models.Model):
    hora = models.CharField(max_length=200)
    wats = models.CharField(max_length=200)
    sound_system = models.CharField(max_length=200)
    tv = models.CharField(max_length=200)
    play = models.CharField(max_length=200)
    computer = models.CharField(max_length=200)
    clothes_iron = models.CharField(max_length=200)
    clothes_wash = models.CharField(max_length=200)
    refrigerator = models.CharField(max_length=200)
    oven = models.CharField(max_length=200)
    estado = models.IntegerField(max_length=200)

    class Meta:
      db_table = "Desagregacion"
