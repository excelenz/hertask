from flask import request
from flask_restful import Resource
from Model import db, Organisation, OrganisationSchema

organisations_schema = OrganisationSchema(many=True)
organisation_schema = OrganisationSchema()

class OrganisationResource(Resource):
    def get(self):
        organisations = Organisation.query.all()
        organisations = organisations_schema.dump(organisations).data
        return {'status': 'success', 'data': organisations}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        data, errors = organisation_schema.load(json_data)
        if errors:
            return errors, 422
        organisation = Organisation.query.filter_by(name=data['name']).first()
        if organisation:
            return {'message': 'Organisation already exists'}, 400
        organisation = Organisation(
            name=json_data['name'],
            address=json_data['address'],
            phone=json_data['phone'],
            pic = json_data['pic']
            )

        db.session.add(organisation)
        db.session.commit()

        result = organisation_schema.dump(organisation).data

        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        data, errors = organisation_schema.load(json_data)
        if errors:
            return errors, 422
        organisation = Organisation.query.filter_by(id=data['id']).first()
        if not organisation:
            return {'message': 'Organisation does not exist'}, 400
        organisation.name = data['name']
        organisation.address = data['address']
        organisation.phone = data['phone']
        organisation.pic = data['pic']

        db.session.commit()

        result = organisation_schema.dump(organisation).data

        return { "status": 'success', 'data': result }, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        data, errors = organisation_schema.load(json_data)
        if errors:
            return errors, 422
        organisation = Organisation.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = organisation_schema.dump(organisation).data

        return { "status": 'success', 'data': result}, 204

