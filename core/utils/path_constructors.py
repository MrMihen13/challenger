from core.models import Sticker, Widget


def path_to_widget(instance: Widget, file) -> str:
    return f'widgets/{instance.pk}/{file}'


def path_to_sticker(instance: Sticker, file) -> str:
    return f'stickers/{instance.sticker_pack.name}/{file}'
