from flask import Blueprint
import pyslurm

api_bp = Blueprint('api_bp', __name__) # "API Blueprint"
@api_bp.route("/greeting") # Blueprints don't use the Flask "app" context. They use their own blueprint's
def greeting():
    return {'name': 'Hello from Flask!'}


@api_bp.route("/submit") # Blueprints don't use the Flask "app" context. They use their own blueprint's
def submit():
    jobs = pyslurm.Jobs.load()
    jobs = list(jobs.keys())
    return {'jobs': jobs}

