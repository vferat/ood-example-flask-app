import os
from flask import Blueprint
from flask import request

from jinja2 import Template

import pyslurm


def render_template(template_path, context):
    output_path = os.path.join(os.getcwd(), 'run.sh')
    # Read template
    with open(template_path) as file:
        template = Template(file.read())
    # Render template
    rendered_script = template.render(context)
    # Write rendered template to file
    with open(output_path, 'w') as file:
        file.write(rendered_script)
    return template.render(output_path)


scripts_folder = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../apps'))


api_bp = Blueprint('api_bp', __name__) # "API Blueprint"
@api_bp.route("/greeting") # Blueprints don't use the Flask "app" context. They use their own blueprint's
def greeting():
    return {'name': 'Hello from Flask!'}


@api_bp.route("/submit", methods = ['GET', 'POST']) # Blueprints don't use the Flask "app" context. They use their own blueprint's
def submit():
    if request.method == 'POST':
        data = request.get_json()
        bids_dir = data['bids_dir']

        template_path = os.path.join(scripts_folder, 'fmriprep', 'script.sh')
        context = {
            'bids_dir': bids_dir}
        rendered_script = render_template(template_path, context)
        try:
            desc = pyslurm.JobSubmitDescription(
                name="test-job",
                cpus_per_task=1,
                script=rendered_script)
            job_id = desc.submit()
        except Exception as e:
            return {'job': str(rendered_script) + ' ' + str(e)}
        return {'job': job_id}

