from django.conf import settings
from django.utils.translation import get_language, ugettext_lazy as _


def is_multilingual():
    return 'cmsplugin_blog.middleware.MultilingualBlogEntriesMiddleware' in settings.MIDDLEWARE_CLASSES


def get_lang_name(lang):
    return _(dict(settings.LANGUAGES)[lang])


def add_current_root(url):
    if is_multilingual():
        new_root = "/%s" % get_language()
        url = new_root + url
    return url
