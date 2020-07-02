from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import datetime

ma = Marshmallow()
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True) 
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Herolo(db.Model):
    __tablename__ = 'herolo_messages'
    message_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer)
    reciever_id = db.Column(db.Integer)
    message =  db.Column(db.String(300))
    subject =  db.Column(db.String(300))
    date = db.Column(db.DateTime)
    status = db.Column(db.Integer)


    def __init__(self, message_id, sender_id, reciever_id, message, subject,status=0):
        self.message_id = message_id
        self.sender_id = sender_id
        self.reciever_id = reciever_id
        self.message = message
        self.subject = subject
        self.date = datetime.datetime.now()
        self.status=status

class Herolousers(db.Model):
    __tablename__ = 'herolo_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    privat_key = db.Column(db.Integer)

    def __init__(self, id, name,privat_key):
        self.id=id
        self.name=name
        self.privat_key=privat_key

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
