from flask import request
from flask_restful import Resource
from Model import db, Herolo,Herolousers, HeroloSchema, HerolousersSchema
import datetime

entries_schema = HeroloSchema(many=True)
entry_schema = HeroloSchema()

class HeroloSingle(Resource):

    def get(self,message_id,user_id,key=0):
        message = Herolo.query.filter((Herolo.reciever_id==user_id) | (Herolo.sender_id==user_id)).first()
        print(message)
        messages = entries_schema.dump(message).data
        return {'status': 'success', 'data': 'READ'}, 200
        pass

    def delete(self, message_id):
        entries=Herolo.query.filter_by(reciever_id = user_id,status=status_list[status]).all()
        entries = entries_schema.dump(entries).data
        return {'status': 'success', 'data': 'DELETE'}, 200
        pass

class HeroloResource(Resource):

    def get(self,user_id=0,status='all'):
        if user_id ==0:
            entries = Herolo.query.all()
            entries = entries_schema.dump(entries).data
            return {'status': 'success', 'data': entries}, 200
        else:
            status_list={'all':3,'unread':0,'read':1}
            if status=='all':
                entries=Herolo.query.filter_by(reciever_id = user_id).all()
            elif status in status_list:
                entries=Herolo.query.filter_by(reciever_id = user_id,status=status_list[status]).all()
            entries = entries_schema.dump(entries).data
            return {'status': 'success', 'data': entries}, 200
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
