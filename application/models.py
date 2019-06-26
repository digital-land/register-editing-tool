from application.extensions import db
from datetime import datetime

class DynamicModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.String(100), nullable=False)
    entry_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    json_blob = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"DynamicModel('{self.id}','{self.schema}', '{self.entry_date}', '{self.json_blob}')"

