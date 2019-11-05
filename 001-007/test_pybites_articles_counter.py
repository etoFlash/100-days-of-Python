import pytest
import requests

from pybites_articles_counter import count_articles, default_url


def test_count_articles_ge_one():
    expected = 1
    assert count_articles() >= expected


def test_count_articles():
    expected = 129
    assert count_articles(address="test_pybites_articles_counter/test_data.html", local=True) == expected


def test_count_articles_raise_404():
    with pytest.raises(requests.exceptions.HTTPError):
        count_articles(default_url[:-1])
