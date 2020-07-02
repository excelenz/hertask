from flask import Blueprint
from flask_restful import Api
from resources.HeroloMsg import HeroloResource,HeroloSingle

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


routes = [
    '/admin/',                              #show all messages
    '/user/<int:user_id>/<status>/'     #show messages for user_id {all,unread}
]
routesSingle=[
    '/delete/message_id/<int:message_id>/user_id/<int:user_id>/',
    '/read/message_id/<int:message_id>/user_id/<int:user_id>/'
]
api.add_resource(HeroloResource, *routes)
api.add_resource(HeroloSingle, *routesSingle)
