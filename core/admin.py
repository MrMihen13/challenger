from django.contrib import admin

from core import models


admin.site.register(models.User)
admin.site.register(models.Document)
admin.site.register(models.Markdown)
admin.site.register(models.Sticker)
admin.site.register(models.StickerPack)
admin.site.register(models.VoiceMessage)
