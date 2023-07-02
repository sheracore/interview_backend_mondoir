from .enums import BioTypeEnum
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_bio_content(bio_type_name: str, bio_content: str):
    try:
        BioTypeEnum(bio_type_name).convert_value_method(bio_content)
    except Exception as e:
        raise ValidationError(
            {"content": [_(f"Invalid value for {bio_type_name}")]}
        ) from e
