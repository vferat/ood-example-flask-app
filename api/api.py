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
    return (output_path)


scripts_folder = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../apps'))


api_bp = Blueprint('api_bp', __name__) # "API Blueprint"
@api_bp.route("/greeting")
def greeting():
    return {'name': 'Hello from Flask!'}


@api_bp.route("/submit", methods=['POST'])
def submit():
    data = request.get_json()
    bids_dir = data['bidsDir']

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
        return {'job_id': job_id}
    except Exception as e:
        return {'Error': str(rendered_script) + ' ' + str(e)}
        

