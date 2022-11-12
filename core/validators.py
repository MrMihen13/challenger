from django.core.exceptions import ValidationError


def image_size_validator(file_obj):
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f'Максимальной размер файла {megabyte_limit}MB')

