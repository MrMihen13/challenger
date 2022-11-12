from django.db.models import QuerySet

from core.serializers import StickerSerializer, StickerPackSerializer


def stickers_pack_formatter(stickers: QuerySet, stickers_packs: QuerySet) -> list[dict]:
    data = []

    for sticker_pack in stickers_packs:
        _stickers = stickers.filter(sticker_pack=sticker_pack).all()

        serializer = StickerPackSerializer(sticker_pack)
        name = serializer.data['name']

        data.append({name: list()})

        for sticker in _stickers:
            serializer = StickerSerializer(sticker)
            data[name].append(serializer.data)

    return data
