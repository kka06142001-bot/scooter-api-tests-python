# Королёв Кирилл, 46-я когорта — Финальный проект. Инженер по тестированию

import requests

from data import ORDER_DATA
from helpers.api import create_order, get_order_by_track


BASE_URL = "https://5069c3af-9001-4faa-9988-1ead9f81ffdb.serverhub.praktikum-services.ru"


def test_create_order():
    response = create_order(BASE_URL, ORDER_DATA)

    assert response.status_code == 201


def test_get_created_order_by_track():
    response = create_order(BASE_URL, ORDER_DATA)

    assert response.status_code == 201

    track = response.json()["track"]

    response = get_order_by_track(BASE_URL, track)

    assert response.status_code == 200