from django.db import models


class Animais(models.Model):
    animal_nome = models.TextField()
    animal_raca = models.TextField()
    animal_peso = models.FloatField()

    def __str__(self):
        return self.animal_nome

# Create your models here.
