import json

from flask import Flask, Response
from marshmallow import ValidationError

from app.api import tickets_router
from app.db import db_session, init_db


def close_session(response: Response) -> Response:
    db_session.remove()
    return response


def handle_validation_error(error: ValidationError) -> [dict, int]:
    return {"message": json.dumps(error.messages)}, 422


def create_app() -> Flask:
    flask_app = Flask(__name__)
    init_db()
    flask_app.register_blueprint(tickets_router)
    flask_app.after_request(close_session)
    flask_app.register_error_handler(ValidationError, handle_validation_error)
    return flask_app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
