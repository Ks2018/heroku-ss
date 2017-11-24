from django.db import models


class Screening(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
    title = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    time = models.CharField(max_length=5)
    age = models.CharField(max_length=5)