import controllers.auth as auth_blueprint
import controllers.user as user_blueprint
from flask import Flask

app = Flask(__name__)
app.register_blueprint(user_blueprint.user)

app.register_blueprint(auth_blueprint.auth)


if (__name__ == '__main__'):
    app.run('localhost', 8000, True)
