from django.db import models


class Screening(models.Model):
    created = models.DateTimeField('date created', auto_now_add=True)
    cinema = models.CharField(max_length=50)
    title = models.CharField(max_length=100, unique=True)
    datetime = models.DateTimeField()
    age = models.CharField(max_length=5)
