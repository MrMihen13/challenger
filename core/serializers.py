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
    ...  # TODO fields all


class VoiceMessageSerializer(serializers.ModelSerializer):
    ...  # TODO fields all


class DocumentSerializer(serializers.ModelSerializer):
    ...  # TODO fields all
