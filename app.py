from flask import Flask
from api.api import api_bp
from client.client import client_bp


app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api_v1')
app.register_blueprint(client_bp, url_prefix='')


if __name__ == "__main__":
	app.run(port=5006, debug=True)
