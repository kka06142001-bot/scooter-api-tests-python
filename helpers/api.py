import requests

from data import BASE_URL, ORDER_DATA


def create_order():
    return requests.post(
        f"{BASE_URL}/api/v1/orders",
        json=ORDER_DATA
    )


def get_order_by_track(track):
    return requests.get(
        f"{BASE_URL}/api/v1/orders/track",
        params={"t": track}
    )
