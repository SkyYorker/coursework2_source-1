from flask import Flask

from posts.views import posts_blueprint
from api.views import api_blueprint
from logger import create_logger

app = Flask(__name__)



create_logger()

app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
