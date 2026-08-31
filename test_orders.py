# Королёв Кирилл, 46-я когорта — Финальный проект. Инженер по тестированию
import requests


BASE_URL = "https://87c455e5-ebb9-4c6e-9167-8a7921677fcd.serverhub.praktikum-services.ru"


def test_create_and_get_order():
    order_data = {
        "firstName": "Kirill",
        "lastName": "Test",
        "address": "Москва, улица Тестовая, 1",
        "metroStation": 4,
        "phone": "+7 800 555 35 35",
        "rentTime": 5,
        "deliveryDate": "2026-09-01",
        "comment": "Pytest API test",
        "color": ["BLACK"]
    }

    response = requests.post(
        f"{BASE_URL}/api/v1/orders",
        json=order_data
    )

    assert response.status_code == 201

    track = response.json()["track"]
    print(f"Создан заказ с треком: {track}")

    response = requests.get(
        f"{BASE_URL}/api/v1/orders/track",
        params={"t": track}
    )

    assert response.status_code == 200

    order = response.json()["order"]

    assert order["track"] == track
    assert order["firstName"] == "Kirill"
    assert order["lastName"] == "Test"