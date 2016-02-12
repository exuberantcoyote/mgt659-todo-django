from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=50, unique='true')
    name = models.CharField(max_length=50)
    hashPassword = models.CharField(max_length=50)

    def _str_(self):
        return self.name

class Task(models.Model):
    owner = models.IntegerField()
    isOwner = models.BooleanField(default='false')
    title = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000, blank='true')
    isComplete = models.BooleanField(default='false')
    collaborator1 = models.EmailField(max_length=50, blank='true')
    collaborator2 = models.EmailField(max_length=50, blank='true')
    collaborator3 = models.EmailField(max_length=50, blank='true')

    def _str_(self):
        return self.title