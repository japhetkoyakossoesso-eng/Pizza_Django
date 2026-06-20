from django.db import models

class Pizza(models.Model):
    nom = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)