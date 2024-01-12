from rest_framework.request import Request


def get_host_from_request(request: Request) -> str:
    """Получить host из запроса."""
    protocol = 'https' if request.is_secure() else 'http'
    return f'{protocol}://{request.get_host()}'
