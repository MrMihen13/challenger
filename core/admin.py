from django.contrib import admin

from core import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['userId', 'role']


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(models.Markdown)
class MarkdownAdmin(admin.ModelAdmin):
    list_display = ['pk']


@admin.register(models.StickerPack)
class StickerPackAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(models.Sticker)
class StickerAdmin(admin.ModelAdmin):
    list_display = ['pk', ]


@admin.register(models.VoiceMessage)
class VoiceMessage(admin.ModelAdmin):
    list_display = ['id', 'user']
