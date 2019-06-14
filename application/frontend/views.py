import requests
from flask import Blueprint
from flask import render_template, current_app, url_for, request, redirect
from application.utils import update_csv, csv_view
from application.forms import formfactory

frontend = Blueprint('frontend', __name__, template_folder='templates')


@frontend.route('/')
def index():
    resp = requests.get(current_app.config['SCHEMA_API_URL'])
    resp.raise_for_status()
    schemas = [schema['name'] for schema in resp.json()]
    return render_template('index.html', schemas=schemas)


@frontend.route('/<schema>', methods=['GET', 'POST'])
def dynamic_form(schema):
    schema_url = f"{current_app.config['SCHEMA_URL']}/{schema}-schema.json"
    draft_file_name = "draft-" + schema
    title = schema.replace('-', ' ').capitalize()
    schema_json = requests.get(schema_url).json()
    form_object = formfactory(schema_json)
    if request.method == 'POST':
        form = form_object(obj=request.form)
        if form.validate():
            update_csv(draft_file_name, form.data)
            row_count = sum(1 for row in csv_view(draft_file_name))
            return redirect(url_for('frontend.check', schema=schema, row=row_count))
    else:
        form = form_object()

    return render_template('dynamicform.html', form=form, schema=schema, title=title)