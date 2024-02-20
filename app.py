import os
from flask import Flask, render_template

MyApp = Flask(__name__)

@MyApp.route("/")
def hello():

	home = os.path.expanduser("~")
	data = os.listdir(home)

	return render_template('index.html', data=data)

if __name__ == "__main__":
	MyApp.run()
