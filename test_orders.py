import pytest

from helpers.api import create_order, get_order_by_track


@pytest.fixture
def order_track():
    response = create_order()
    return response.json()["track"]


def test_create_order():
    response = create_order()
    assert response.status_code == 201


def test_get_created_order_by_track(order_track):
    response = get_order_by_track(order_track)
    assert response.status_code == 200
