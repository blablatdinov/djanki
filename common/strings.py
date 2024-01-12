import random
import string


def generate_random_string(length: int = 16) -> str:
    """Генерация рандомной строки.

    Включает в себя: английские символы в верхнем и нижних регистрах и символы
    """
    return ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length)
    )


def generate_random_code_of_numbers(length: int = 4) -> str:
    """Сгенерировать код из цифр."""
    return ''.join(random.choice(string.digits) for _ in range(length))
