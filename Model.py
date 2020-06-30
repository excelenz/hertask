from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import datetime

ma = Marshmallow()
db = SQLAlchemy()

class Herolo(db.Model):
    __tablename__ = 'herolo_messages'
    message_id = db.Column(db.Integer, primary_key=True)
    sender_id =  db.Column(db.Integer, db.ForeignKey('herolo_users.id', ondelete='SET NULL'))
    reciever_id = db.Column(db.Integer, db.ForeignKey('herolo_users.id', ondelete='SET NULL'))
    message =  db.Column(db.String(300))
    subject =  db.Column(db.String(300))
    date = db.Column(db.DateTime)

    def __init__(self, message_id, sender_id, reciever_id, message, subject):
        self.message_id = message_id
        self.sender_id = sender_id
        self.reciever_id = reciever_id
        self.message = message
        self.subject = subject
        self.date = datetime.datetime.now()

class Herolousers(db.Model):
    __tablename__ = 'herolo_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)

    def __init__(self, id, name):
        self.id=id
        self.name=name

class telegram(db.Model):
    __tablename__ = 'telegram_messages'
    message_id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer)
    chat_title = db.Column(db.String(240))
    user_id = db.Column(db.Integer)
    first_name = db.Column(db.String(240))
    username = db.Column(db.String(240))
    date = db.Column(db.DateTime)
    text = db.Column(db.String(300))

    def __init__(self, message_id, chat_id, chat_title, user_id, first_name,username,date,text):
        self.message_id = message_id
        self.chat_id = chat_id
        self.chat_title = chat_title
        self.user_id = user_id
        self.first_name = first_name
        self.username = username
        self.date = date
        self.text = text



class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(240))
    phone = db.Column(db.String(20))
    org_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete='SET NULL'))
    pic = db.Column(db.String(300))

    def __init__(self, name, address, phone, org_id, pic):
        self.name = name
        self.address = address
        self.phone = phone
        self.org_id = org_id
        self.pic = pic

class Organisation(db.Model):
    __tablename__ = 'organisations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    address = db.Column(db.String(240))
    phone = db.Column(db.String(20))
    pic = db.Column(db.String(300))

    def __init__(self, name, address, phone, pic):
        self.name = name
        self.address = address
        self.phone = phone
        self.pic = pic

class EntrySchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    address = fields.String()
    phone = fields.String()
    org_id = fields.Integer()
    pic = fields.String()

class OrganisationSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    address = fields.String()
    phone = fields.String()
    pic = fields.String()


class telegramSchema(ma.Schema):
    message_id =  fields.Integer()
    chat_id =  fields.Integer()
    chat_title = fields.String()
    user_id =  fields.Integer()
    first_name = fields.String()
    username =  fields.String()
    date =  fields.DateTime()
    text = fields.String()


class HeroloSchema(ma.Schema):
    message_id =  fields.Integer()
    sender_id =  fields.Integer()
    reciever_id = fields.Integer()
    message =  fields.String()
    subject = fields.String()
    date = fields.DateTime()


class HerolousersSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()