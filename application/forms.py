import re
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField
from wtforms.validators import ValidationError, DataRequired, Optional, URL, Email
from wtforms.fields.html5 import DateField



types_to_form_fields = {'string': StringField, 'date': DateField, 'number': DecimalField, 'select': SelectField}


def formfactory(schema):

    class DynamicForm(FlaskForm):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

    for field in schema.get('fields'):
        constraints = field.get('constraints')
        form_field = form_field_creator(field, constraints)
        if form_field is not None:
            validators = validators_builder(field)
            choices = select_field_choices(form_field, constraints)
            form = create_field(form_field, field, validators, choices)
            setattr(DynamicForm, field['name'], form)

    return DynamicForm


def form_field_creator(field, constraints):
    if constraints.get('pattern') and '|' in constraints.get('pattern'):
        form_field = types_to_form_fields.get('select')
    else:
        form_field = types_to_form_fields.get(field.get('type'))
    return form_field


def type_validators(format_type):
    if format_type is not None:
        return {
            "uri" : URL(message="This is not a valid URL"),
            "email" : Email(message="This is not a valid email address")
        }[format_type]


def validators_builder(field):
    constraints = field.get('constraints')
    validators = []
    if field.get('format') is not None:
        validators.append(type_validators(field.get('format')))
    if constraints.get('required'):
        validators.append(DataRequired(message="This field is required"))
    else:
        validators.append(Optional(strip_whitespace=True))
    return validators


def select_field_choices(form_field, constraints):
    if form_field == SelectField:
        choice_string = constraints.get('pattern')
        choice_array = re.sub('[(){}<>]', '', choice_string).split('|')
        choices = []
        for choice in choice_array:
            title = choice.replace('-', ' ').capitalize()
            choices.append((choice, title))
        return choices


def create_field(form_field, field, validators, choices=None):
    if form_field == SelectField:
        form = form_field(field['title'], choices=choices, validators=validators)
    else:
        form = form_field(field['title'], validators=validators)
    return form
