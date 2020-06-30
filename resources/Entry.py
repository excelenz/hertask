from flask import request
from flask_restful import Resource
from Model import db, Entry, EntrySchema

entries_schema = EntrySchema(many=True)
entry_schema = EntrySchema()

class EntryResource(Resource):
    def get(self):
        entries = Entry.query.all()
        entries = entries_schema.dump(entries).data
        return {'status': 'success', 'data': entries}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        data, errors = entry_schema.load(json_data)
        if errors:
            return errors, 422
        entry = Entry.query.filter_by(name=data['name']).first()
        if entry:
            return {'message': 'Entry already exists'}, 400
        entry = Entry(
            name=json_data['name'],
            address=json_data['address'],
            phone=json_data['phone'],
            org_id=json_data['org_id'],
            pic=json_data['pic']
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
        entry = Entry.query.filter_by(id=data['id']).first()
        if not entry:
            return {'message': 'Entry does not exist'}, 400
        entry.name = data['name']
        entry.address = data['address']
        entry.phone = data['phone']
        entry.org_id = data['org_id']
        entry.pic = data['pic']

        db.session.commit()

        result = entry_schema.dump(entry).data

        return { "status": 'success', 'data': result }, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        data, errors = entry_schema.load(json_data)
        if errors:
            return errors, 422
        entry = Entry.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = entry_schema.dump(entry).data

        return { "status": 'success', 'data': result}, 204

