from django.shortcuts import get_object_or_404

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.generics import views
from rest_framework import response, status, permissions

from core.models import Markdown, Document, StickerPack, Sticker, VoiceMessage
from core.serializers import DocumentSerializer, MarkdownSerializer, VoiceMessageSerializer
from core.third_party_api.documents_api import DocumentAPI
from core.third_party_api.alphavantage_api import AlphavantageAPI
from core.utils.formatters import stickers_pack_formatter


class DocumentApiView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        operation_description="Get document",
        ponses={
            201: openapi.Response(
                description='Document data',
                schema=DocumentSerializer()
            )
        }
    )
    def get(self, request, document_id=None, *args, **kwargs):
        queryset = get_object_or_404(Document, pk=document_id)
        document = DocumentSerializer(queryset)
        return response.Response(data=document.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Subscribe document",
        responses={
            201: openapi.Response(
                description='Request successfully created',
            )
        }
    )
    def post(self, *args, **kwargs):
        document_api = DocumentAPI()
        return response.Response(data=document_api.subscribe_document(), status=status.HTTP_201_CREATED)


class MarkdownApiView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        operation_description="Save markdown",
        request_body=openapi.Schema(
            description="Markdown text",
            type=openapi.TYPE_OBJECT,
            properties={
                'text': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['text'],
        ),
        responses={
            201: openapi.Response(
                description='Markdown data',
                schema=MarkdownSerializer()
            ),
            400: openapi.Response(
                description='Bad request'
            )
        }
    )
    def post(self, request, *args, **kwargs):
        text = self.request.POST['text']
        serializer = MarkdownSerializer(data=text)
        if serializer.is_valid():
            return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Get markdown",
        manual_parameters=[
            openapi.Parameter(
                type=openapi.TYPE_INTEGER, in_=openapi.IN_QUERY, name='id', required=True,
                description='Markdown file id'
            )
        ],
        responses={
            201: openapi.Response(
                description='Markdown data',
                schema=MarkdownSerializer()
            )
        }
    )
    def get(self, request, file_id, *args, **kwargs):
        queryset = get_object_or_404(Markdown, id=file_id)
        file = MarkdownSerializer(queryset)
        return response.Response(data=file.data, status=status.HTTP_200_OK)


class StickersApiView(views.APIView):
    @swagger_auto_schema(
        operation_description="Get sticker packs",
        responses={
            201: openapi.Response(
                description='Stickers data',
            )
        }
    )
    def get(self, request, *args, **kwargs):
        stickers = Sticker.objects.all()
        stickers_packs = StickerPack.objects.all()

        data = stickers_pack_formatter(stickers, stickers_packs)

        return response.Response(data=data, status=status.HTTP_200_OK)


class VoiceMessageApiView(views.APIView):
    @swagger_auto_schema(
        operation_description="Save message",
        request_body=openapi.Schema(
            description="Markdown text",
            type=openapi.TYPE_OBJECT,
            properties={
                'message': openapi.Schema(type=openapi.TYPE_FILE),
            },
            required=['message'],
        ),
        responses={
            201: openapi.Response(
                description='Markdown data',
                schema=MarkdownSerializer()
            ),
            400: openapi.Response(
                description='Bad request'
            )
        }
    )
    def post(self, request, dialogId):
        for filename, file in request.FILES.iteritems():
            voice = VoiceMessage()
            voice.message = file
            voice.user = self.request.user
            voice.dialogId = dialogId
            voice.save()
        return response.Response(status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Voice message packs",
        manual_parameters=[
            openapi.Parameter(
                type=openapi.TYPE_INTEGER, in_=openapi.IN_QUERY, name='id', required=True,
                description='Id'
            )
        ],
        responses={
            201: openapi.Response(
                description='Voice message data',
                schema=VoiceMessageSerializer()
            )
        }
    )
    def get(self, request, dialogId=None):
        voice_message_id = request.query_params.get('id', None)

        voice_messages = VoiceMessage.objects.filter(dialogId=dialogId).all()

        if voice_messages:
            voice_messages = voice_messages.filter(id=voice_message_id)
            voice = VoiceMessageSerializer(voice_messages, many=True)
        else:
            voice = VoiceMessageSerializer(voice_messages)

        return response.Response(voice.data, status=status.HTTP_200_OK)


class GetNewsApiView(views.APIView):
    permission_classes = (permissions.IsAuthenticated, )

    @swagger_auto_schema(
        operation_description="Get news data",
        responses={
            201: openapi.Response(
                description='News data',
            )
        }
    )
    def get(self, request, *args, **kwargs):
        alphavantage_api = AlphavantageAPI()
        data = alphavantage_api.get_news()

        return response.Response(data=data, status=status.HTTP_200_OK)


class GetTrendsApiView(views.APIView):
    permission_classes = (permissions.IsAuthenticated, )

    @swagger_auto_schema(
        operation_description="Get news data",
        responses={
            201: openapi.Response(
                description='News data',
            )
        }
    )
    def get(self, request, *args, **kwargs):
        alphavantage_api = AlphavantageAPI()
        data = alphavantage_api.get_trends()

        return response.Response(data=data, status=status.HTTP_200_OK)
