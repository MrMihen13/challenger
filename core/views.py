from rest_framework.generics import views
from rest_framework import response, status

from core.models import Markdown, Document, StickerPack, Sticker, VoiceMessage


class DocumentApiView(views.APIView):
    ...


class MarkdownApiView(views.APIView):
    ...


class StickersApiView(views.APIView):
    ...


class VoiceMessageApiView(views.APIView):
    ...
