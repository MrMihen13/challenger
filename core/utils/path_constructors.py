def path_to_widget(instance, file) -> str:
    return f'widgets/{instance.name}/{file}'


def path_to_sticker(instance, file) -> str:
    return f'stickers/{instance.sticker_pack.name}/{file}'


def path_to_voice_message(instance, file) -> str:
    return f'voice_massage/{instance.user.pk}/{file}'
