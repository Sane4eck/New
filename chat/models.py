from django.db import models


class Massage(models.Model):
    user_id = models.CharField('Айди автора', max_length=100)
    text = models.TextField()
    time = models.DateTimeField()


class Chat(models.Model):
    name = models.CharField('Имя автора', max_length=100)
    description = models.TextField()
