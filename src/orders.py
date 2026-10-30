"""Расчёт суммы позиции заказа."""


def total(price, quantity):
    """Цена умножается на неотрицательное количество."""
    if price < 0 or quantity < 0:
        raise ValueError("Цена и количество не должны быть отрицательными")
    return price * quantity
