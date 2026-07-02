def calc(model_price, c):
    discount = 0

    if c["screen"] == "yes":
        discount += 0.30
    if c["battery"] == "yes":
        discount += 0.10
    if c["camera"] == "yes":
        discount += 0.10
    if c["faceid"] == "yes":
        discount += 0.15
    if c["body"] == "yes":
        discount += 0.10

    min_price = int(model_price * 0.35)
    price = int(model_price * (1 - discount))

    return max(price, min_price)