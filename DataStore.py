from dataclasses import dataclass


@dataclass
class Restaurant:
    restaurant_id: int
    name: str
    address: str
    menu_items: int
    menu: list[dict]


class DataStore:
    RESTAURANTS: dict[int, Restaurant] = {}
