import time

from DataStore import DataStore, Restaurant

from flask import Flask, request

flask_app = Flask(__name__)


@flask_app.route('/register', methods=['POST'])
def register_restaurant():
    payload = request.get_json()
    restaurant = Restaurant(
        restaurant_id=payload['restaurant_id'],
        name=payload['name'],
        address=payload['address'],
        menu_items=payload['menu_items'],
        menu=payload['menu']
    )
    DataStore.RESTAURANTS[payload['restaurant_id']] = restaurant
    print(
        f'Restaurant {restaurant.name} at {restaurant.address} registered successfully!!!')
    return {'status_code': 200}


@flask_app.route('/menu', methods=['GET'])
def get_menu():
    return {
        'restaurants': len(DataStore.RESTAURANTS),
        'restaurants_data': [{
            'name': restaurant.name,
            'menu_items': restaurant.menu_items,
            'menu': restaurant.menu,
            'restaurant_id': restaurant.restaurant_id
        } for restaurant in DataStore.RESTAURANTS.values()]
    }


@flask_app.route('/order', methods=['POST'])
def post_order():
    payload = request.get_json()
    print(f'Food Ordering received: {payload}')
    body = {
        "order_id": None,
        "orders": [{
            "restaurant_id": order['restaurant_id'],
            "restaurant_address": DataStore.RESTAURANTS[order['restaurant_id']].address,
            "order_id": None,
            "registered_time": int(time.time())
        } for order in payload['orders']]
    }

    return body
