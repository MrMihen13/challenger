from django.urls import path

from core import views


urlpatterns = [
    path('document/<int:document_id>', views.DocumentApiView.as_view()),
    path('voice_messages/<int:dialogId>', views.VoiceMessageApiView),
    path('stickers', views.StickersApiView.as_view()),
    path('markdown', views.MarkdownApiView.as_view()),
    path('news', views.GetNewsApiView.as_view()),
    path('trends', views.GetTrendsApiView.as_view())
]
