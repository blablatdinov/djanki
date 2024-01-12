import pytest
from bs4 import BeautifulSoup as bs

pytestmark = [pytest.mark.django_db]


@pytest.fixture()
def posts(mixer):
    return mixer.cycle(15).blend('blog.Post')


def test(client, posts):
    got = client.get('/')

    soup = bs(got.content, 'lxml')

    assert got.status_code == 200
    assert [el.text for el in soup.find_all('p')] == [p.name for p in posts]
