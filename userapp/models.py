from django.contrib.auth.models import User
from django.db import models
from asosiyapp.models import *

class Sotuvchi(models.Model):
    ism = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=90)
    tel = models.CharField(max_length=20)
    user = models.ManyToManyField(User)
    def __str__(self):
        return f"{self.ism}, {self.nom}, {self.manzil}"