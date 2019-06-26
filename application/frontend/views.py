import requests
import datetime
from flask import Blueprint
from flask import render_template, current_app, url_for, request, redirect

from application.models import DynamicModel
from application.utils import json_serialiser, remove_dashes, convert_ordered_dicts_for_dl
from application.forms import formfactory
from application.extensions import db

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
    title = schema.replace('-', ' ').capitalize()
    schema_json = requests.get(schema_url).json()
    form_object = formfactory(schema_json)
    if request.method == 'POST':
        form = form_object(obj=request.form)
        if form.validate():
            entry_data = form.data
            del entry_data['csrf_token']
            entry = DynamicModel(schema=schema, json_blob=json_serialiser(entry_data))
            db.session.add(entry)
            db.session.commit()
            obj = db.session.query(DynamicModel).order_by(DynamicModel.id.desc()).first()
            return redirect(url_for('frontend.check', schema=schema, row=obj.id))
    else:
        form = form_object()

    return render_template('dynamicform.html', form=form, schema=schema, title=title)


@frontend.route('/<schema>/<row>/check')
def check(schema, row):
    entry = DynamicModel.query.filter_by(id=row).first()
    print(entry.json_blob)
    title = remove_dashes(schema)
    data_list = convert_ordered_dicts_for_dl(entry.json_blob)

    return render_template('check.html', data=data_list, title=title)

@frontend.route('/<schema>/<row>/edit')
def edit(schema, row):
    schema = schema
    schema_url = f"{current_app.config['SCHEMA_URL']}/{schema}-schema.json"
    schema_json = requests.get(schema_url).json()
    form_object = formfactory(schema_json)
    entry = DynamicModel.query.filter_by(id=row).first()
    data = entry.json_blob
    for k, v in data.items():
        if "date" in k and v is not None:
            data[k] = datetime.datetime.strptime(v, '%Y-%m-%d').date()
    title = "Editing the form"
    form = form_object(**data)

    return render_template('dynamicform.html', form=form, schema=schema, title=title)

