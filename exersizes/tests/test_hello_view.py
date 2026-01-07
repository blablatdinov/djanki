import pytest

pytestmark = [pytest.mark.django_db]


def test_hello(client):
    got = client.get('/hello')

    assert got.status_code == 200
    assert got.content == b'<h1>Hello, world</h1>'
