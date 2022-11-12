from django.db import models
import uuid


def uniqie_name():
    name = str(uuid.uuid4())
    return f'{name}'


class User(models.Model):
    userId = models.BigAutoField(primary_key=True)


class Widget(models.Model):
    text = models.TextField(blank=False)
    image = models.ImageField(upload_to=f'/images/{uniqie_name()}')


class Sticker(models.Model):
    image_sticker = models.ImageField(upload_to=f'/stickers/{uniqie_name()}')


class StickerPack(models.Model):
    name = models.CharField(max_length=36)
    stickers = models.ManyToManyField(Sticker)


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

