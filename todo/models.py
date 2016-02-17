from __future__ import unicode_literals
from django.core.validators import MaxLengthValidator, MinLengthValidator

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    hashPassword = models.CharField(max_length=50)

    def _str_(self):
        return self.name

class Task(models.Model):
    owner = models.IntegerField()
    isOwner = models.BooleanField(default=False)
    title = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000, blank=True)
    isComplete = models.BooleanField(default=False)
    collaborator1 = models.EmailField(max_length=50, blank=True)
    collaborator2 = models.EmailField(max_length=50, blank=True)
    collaborator3 = models.EmailField(max_length=50, blank=True)

    def _str_(self):
        return self.title