from rest_framework import serializers

from core.models import StickerPack, Sticker, VoiceMessage, Document, Markdown


class StickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sticker
        fields = ['sticker_image']


class StickerPackSerializer(serializers.ModelSerializer):
    stickers_serial = StickerSerializer(many=True)

    class Meta:
        model = StickerPack
        fields = ['name', 'stickers_serial']


class MarkdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Markdown
        fields = ['__all__']


class VoiceMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceMessage
        fields = ['__all__']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['__all__']
