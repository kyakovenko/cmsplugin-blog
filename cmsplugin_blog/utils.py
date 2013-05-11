from django.conf import settings
from django.utils.translation import get_language, ugettext_lazy as _

from models import multilingual_middlewares


def is_multilingual():
    for middleware in multilingual_middlewares:
        if middleware in settings.MIDDLEWARE_CLASSES:
            return True
    return False


def get_lang_name(lang):
    return _(dict(settings.LANGUAGES)[lang])

