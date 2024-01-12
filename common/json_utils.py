import json


def print_test_response_payload(payload: dict) -> None:
    """Печать форматированного json из словаря.

    >>> print_test_response_payload({'hello': 'world'})
    ... {
    ...     'hello': 'world'
    ... }

    Пригождается для тестов:

    from apps.common.json_utils import print_test_response_payload
    print_test_response_payload(got.json())
    assert False
    """
    print(json.dumps(payload, indent=4, sort_keys=True, ensure_ascii=False))  # noqa: T001
