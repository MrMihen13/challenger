from django.db import models
from django.core.validators import FileExtensionValidator

from core.utils.path_constructors import path_to_sticker, path_to_widget, path_to_voice_message
from core.validators import image_size_validator


class User(models.Model):
    class RoleChoices(models.TextChoices):
        CLIENT = 'CLIENT'
        OPERATOR = 'OPERATOR'

    userId = models.BigAutoField(primary_key=True)
    role = models.CharField(max_length=10, choices=RoleChoices.choices, null=False, blank=False, verbose_name='Role')


class Document(models.Model):
    image = models.ImageField(
        upload_to=path_to_widget, blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), image_size_validator]
    )


class Markdown(models.Model):
    text = models.TextField(null=False, blank=False)


class VoiceMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.FileField(upload_to=path_to_voice_message,
                               validators=[FileExtensionValidator(allowed_extensions=['mp3'])])


class StickerPack(models.Model):
    name = models.CharField(max_length=36, blank=False, null=False, unique=True)


class Sticker(models.Model):
    sticker_pack = models.ForeignKey(StickerPack, on_delete=models.CASCADE)
    image_sticker = models.ImageField(
        upload_to=path_to_sticker, blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), image_size_validator]
    )

# class Message(models.Model):
#     class TypeMessageChoice(models.TextChoices):
#         TEXT = "TEXT"
#         MEDIA = "MEDIA"
#         WIDGET = "WIDGET"
#
#     dialogId = models.IntegerField(blank=False)
#     text = models.TextField(blank=False)
#     messageType = models.CharField(max_length=32, choices=TypeMessageChoice.choices)
#     data = models.JSONField(blank=True)
#     mediaUrl = models.URLField(blank=True)
