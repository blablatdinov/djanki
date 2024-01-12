from django.core.cache import cache


class ValueNotFoundInCache(Exception):
    """Запись в редисе не найдена."""

    pass


def search_value_in_cache(value: str) -> str:
    """Поиск ключей в кеше по значению.

    Raises:
        Exception: в случае если ключ не найден
    """
    for key in cache.keys('*'):
        if cache.get(key) == value:
            return key

    raise ValueNotFoundInCache


def delete_rows_from_cache_by_value(value: str) -> None:
    """Удалить все значения в кеше по значению."""
    for key in cache.keys('*'):
        if cache.get(key) == value:
            cache.delete(key)
