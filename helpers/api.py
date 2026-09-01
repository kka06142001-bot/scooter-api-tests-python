import requests


def create_order(base_url, order_data):
    return requests.post(
        f"{base_url}/api/v1/orders",
        json=order_data
    )


def get_order_by_track(base_url, track):
    return requests.get(
        f"{base_url}/api/v1/orders/track",
        params={"t": track}
    )