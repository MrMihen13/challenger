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

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return str(self.userId)


class Document(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True, unique=True)
    image = models.ImageField(upload_to=path_to_widget, blank=True, null=True)

    def __str__(self):
        return self.name


class Markdown(models.Model):
    text = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.pk)


class VoiceMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dialogId = models.IntegerField(null=False, blank=False)
    message = models.FileField(upload_to=path_to_voice_message,
                               validators=[FileExtensionValidator(allowed_extensions=['mp3'])])

    def __str__(self):
        return str(self.pk)


class StickerPack(models.Model):
    name = models.CharField(max_length=36, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name


class Sticker(models.Model):
    sticker_pack = models.ForeignKey(StickerPack, on_delete=models.CASCADE)
    image_sticker = models.ImageField(
        upload_to=path_to_sticker, blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), image_size_validator]
    )

    def __str__(self):
        return str(self.pk)
