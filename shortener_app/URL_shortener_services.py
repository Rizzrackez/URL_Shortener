from django.core.exceptions import ObjectDoesNotExist
import requests

from shortener_app.models import SourceURL


def check_exists_slug(slug: str):
    """Проверка на существующий slug в базе данных"""
    try:
        SourceURL.objects.get(slug=slug)
        return False

    except ObjectDoesNotExist:
        return True


def check_valid_url(url: str):
    """Проверка на существование заданного URL-a"""
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return False
        return True

    except Exception:
        return False
