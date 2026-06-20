from django.db import models

class Pizza(models.Model):
    nom = models.CharField(max_length=400)
    ingredients = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
