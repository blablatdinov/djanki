from enum import Enum
from typing import Tuple


class BaseModelChoicesEnum(Enum):
    """Базовый enum для выбора в CharField."""

    @classmethod
    def choices(cls) -> Tuple[str, str]:
        """Возвращает tuple для аргумента choices."""
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def values(cls) -> Tuple[str]:
        """Значения."""
        return tuple(i.value for i in cls)
