import os
from flask import Blueprint
import pyslurm

scripts_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../scripts')


api_bp = Blueprint('api_bp', __name__) # "API Blueprint"
@api_bp.route("/greeting") # Blueprints don't use the Flask "app" context. They use their own blueprint's
def greeting():
    return {'name': 'Hello from Flask!'}


@api_bp.route("/submit") # Blueprints don't use the Flask "app" context. They use their own blueprint's
def submit():
    script_path = os.path.join(scripts_folder, 'script.sh')
    desc = pyslurm.JobSubmitDescription(
        name="test-job",
        cpus_per_task=1,
        script=script_path)
    job_id = desc.submit()
    return {'job': job_id}

