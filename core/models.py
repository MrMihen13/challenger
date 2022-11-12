from django.db import models


# Create your models here.
class User(models.Model):
    userId = models.BigAutoField(primary_key=True)
    avatar = models.URLField()
    surname = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    middleName = models.CharField(max_length=128)


class Widget(models.Model):
    text = models.TextField()
    image = models.TextField()


class Message(models.Model):
    class TypeMessageChoice(models.TextChoices):
        TEXT = "TEXT"
        MEDIA = "MEDIA"
        WIDGET = "WIDGET"

    dialogId = models.IntegerField(blank=False)
    text = models.TextField(blank=False)
    messageType = models.CharField(max_length=32, choices=TypeMessageChoice.choices)
    data = models.JSONField(blank=True)
    mediaUrl = models.URLField(blank=True)

