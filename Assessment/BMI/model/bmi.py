from .. import db
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Float, String


class BMI(db.Model):
    """model for bmi"""
    __tablename__ = 'bmi'
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    gender = db.Column(String, nullable=False)
    height_cm = db.Column(Float, nullable=False)
    weight_kg = db.Column(Float, nullable=False)
    bmi = db.Column(Float, nullable=False)
    bmi_category = db.Column(String, nullable=False)
    health_risk = db.Column(String, nullable=False)
   