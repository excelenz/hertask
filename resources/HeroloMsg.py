from flask import request
from flask_restful import Resource
from Model import db, Herolo,Herolousers, HeroloSchema, HerolousersSchema
import datetime

entries_schema = HeroloSchema(many=True)
entry_schema = HeroloSchema()

class HeroloResource(Resource):

    def get(self,id=0):
        if id ==0:
            entries = Herolo.query.all()
            entries = entries_schema.dump(entries).data
            return {'status': 'success', 'data': entries}, 200
        else:
            #entry = Herolo.query.filter_by(message_id=data['message_id']).first()
            pass

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        data, errors = entry_schema.load(json_data)
        if errors:
            return errors, 422
        entry = Herolo.query.filter_by(message_id=data['message_id']).first()
        if entry:
            return {'message': 'Entry already exists'}, 400
        entry = Herolo(
            message_id=json_data['message_id'],
            sender_id=json_data['sender_id'],
            reciever_id=json_data['reciever_id'],
            message=json_data['message'],
            subject=json_data['subject'],
            status=0
            )

        db.session.add(entry)
        db.session.commit()

        result = entry_schema.dump(entry).data

        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        data, errors = entry_schema.load(json_data)
        if errors:
            return errors, 422
        entry = Herolo.query.filter_by(id=data['id']).first()
        if not entry:
            return {'message': 'Entry does not exist'}, 400
        entry.message_id = data['message_id']
        entry.chat_id = data['chat_id']
        entry.chat_title = data['chat_title']
        entry.user_id = data['user_id']
        entry.first_name = data['first_name']
        entry.username = data['username']
        entry.date = data['date']
        entry.text = data['text']

        db.session.commit()

        result = entry_schema.dump(entry).data

        return { "status": 'success', 'data': result }, 204
