import os

from application import create_app
from application.extensions import db
from application.api_0_1_0.models import User, UserSession


config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'UserSession': UserSession}


if __name__ == '__main__':
    app.run('0.0.0.0')