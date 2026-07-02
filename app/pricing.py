import json

def load_prices():
    with open("data/prices.json", "r", encoding="utf-8") as f:
        return json.load(f)


def calculate_trade_in(model: str, condition: dict):
    prices = load_prices()
    base = prices.get(model, 50000)

    discount = 0

    if condition.get("screen_crack"):
        discount += 0.30

    if condition.get("face_id_broken"):
        discount += 0.15

    if condition.get("camera_issue"):
        discount += 0.10

    if condition.get("body_damage"):
        discount += 0.10

    if condition.get("battery_low"):
        discount += 0.07

    final_price = int(base * (1 - discount))
    final_price = max(final_price, int(base * 0.3))  # floor

    return final_price


def calculate_upgrade(trade_in_price, new_phone_price=129990):
    doplata = new_phone_price - trade_in_price + 15000
    monthly = doplata // 12

    return doplata, monthly