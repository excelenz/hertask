from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import datetime

ma = Marshmallow()
db = SQLAlchemy()

class Herolousers(db.Model):
    __tablename__ = 'herolo_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)

    def __init__(self, id, name):
        self.id=id
        self.name=name

class Herolo(db.Model):
    __tablename__ = 'herolo_messages'
    message_id = db.Column(db.Integer, primary_key=True)
    sender_id =  db.Column(db.Integer)
    reciever_id = db.Column(db.Integer, db.ForeignKey('herolo_users.id', ondelete='SET NULL'))
    message =  db.Column(db.String(300))
    subject =  db.Column(db.String(300))
    date = db.Column(db.DateTime)
    status = db.Column(db.Integer)
    herolo_users = db.relationship('Herolousers',foreign_keys='herolo_users.id')

    def __init__(self, message_id, sender_id, reciever_id, message, subject,status=0):
        self.message_id = message_id
        self.sender_id = sender_id
        self.reciever_id = reciever_id
        self.message = message
        self.subject = subject
        self.date = datetime.datetime.now()
        self.status=status




class HeroloSchema(ma.Schema):
    message_id =  fields.Integer()
    sender_id =  fields.Integer()
    reciever_id = fields.Integer()
    message =  fields.String()
    subject = fields.String()
    date = fields.DateTime()
    status = fields.Integer()


class HerolousersSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
