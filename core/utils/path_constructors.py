def path_to_widget(instance, file) -> str:
    return f'widgets/{instance.pk}/{file}'


def path_to_sticker(instance, file) -> str:
    return f'stickers/{instance.sticker_pack.name}/{file}'
