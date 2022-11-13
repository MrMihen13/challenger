from rest_framework import serializers

from core.models import StickerPack, Sticker, VoiceMessage, Document, Markdown


class StickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sticker
        fields = ['image_sticker']


class StickerPackSerializer(serializers.ModelSerializer):

    class Meta:
        model = StickerPack
        fields = ['name', ]


class MarkdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Markdown
        fields = ['text', ]


class VoiceMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceMessage
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
