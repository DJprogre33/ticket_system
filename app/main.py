import json

from flask import Flask
from marshmallow import ValidationError

from app.db import db_session, init_db


def close_session(response):
    db_session.remove()
    return response


def handle_validation_error(error):
    return {"message": json.dumps(error.messages)}, 422


def create_app():
    flask_app = Flask(__name__)
    init_db()
    flask_app.after_request(close_session)
    flask_app.register_error_handler(ValidationError, handle_validation_error)
    print("creating flask app")
    return flask_app


app = create_app()

if __name__ == "__main__":
    app.run()
