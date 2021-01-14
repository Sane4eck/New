from django.db import models

class Calculate(models.Model):
    first_number = models.IntegerField()
    second_number = models.IntegerField()
    summa = models.IntegerField()
    division = models.FloatField()
    multiply = models.IntegerField()
    minus = models.IntegerField()
