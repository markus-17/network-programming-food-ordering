from FlaskApp import flask_app
from settings import FOOD_ORDERING_PORT

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=FOOD_ORDERING_PORT, debug=False, use_reloader=False)
