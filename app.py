from flask import Blueprint
from flask_restful import Api
from resources.Entry import EntryResource
from resources.Organisation import OrganisationResource
from resources.Hello import Hello
from resources.JsonTelegram import JsonTelegramResource
from resources.HeroloMsg import HeroloResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# Route
api.add_resource(EntryResource, '/Entry')
api.add_resource(OrganisationResource, '/Org')
api.add_resource(Hello, '/Hello')
api.add_resource(JsonTelegramResource, '/Json')
api.add_resource(HeroloResource, '/Herolo')
