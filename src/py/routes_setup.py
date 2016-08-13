from app import api
from routes.ping import Ping
from routes.client_api import *

api.add_resource(AddressListsRoute, '/api/list')
api.add_resource(MapRoute, '/api/list/<int:list_id>/map')
api.add_resource(Ping, '/populate')
