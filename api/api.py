import os
from flask import Blueprint
import pyslurm

scripts_folder = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../apps'))


api_bp = Blueprint('api_bp', __name__) # "API Blueprint"
@api_bp.route("/greeting") # Blueprints don't use the Flask "app" context. They use their own blueprint's
def greeting():
    return {'name': 'Hello from Flask!'}


@api_bp.route("/submit") # Blueprints don't use the Flask "app" context. They use their own blueprint's
def submit():
    try:
        script_path = os.path.join(scripts_folder, 'fmriprep', 'script.sh')
        desc = pyslurm.JobSubmitDescription(
            name="test-job",
            cpus_per_task=1,
            script=script_path)
        job_id = desc.submit()
    except Exception as e:
        return {'job': str(script_path) + ' ' + str(e)}
    return {'job': job_id}

