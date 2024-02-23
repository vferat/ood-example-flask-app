from flask import Blueprint, render_template

client_bp = Blueprint("client_bp", __name__, # 'Client Blueprint'
    template_folder="templates", # Required for our purposes
    static_folder="vue-app/dist/assets", # Again, this is required
    static_url_path="/client" # Flask will be confused if you don't do this
)

@client_bp.route("/")
def index():
    return render_template("client.html")