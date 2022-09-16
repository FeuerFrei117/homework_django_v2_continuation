from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_name(value):
    if value.isdigit():
        raise ValidationError(
            _(f'Имя не может состоять только из цифр'),
            params={'value': value},
        )
