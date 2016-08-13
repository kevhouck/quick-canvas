from flask_restful import Resource, reqparse, fields, marshal_with
from googlemaps import *
from models.address import *
from models.address_list import *
from math import *
import sys
from algo import *
import json

test_addresses = ["114 N Breese Terrace, Madison, WI, 53726",
 "1615 Hoyt St, Madison, WI, 53726",
 "1714 Van Hise Ave, Madison, WI, 53726",
 "1712 Van Hise Ave, Madison, WI, 53726",
 "1726 Van Hise Ave, Madison, WI, 53726",
 "108 N Spooner St, Madison, WI, 53726",
 "110 N Spooner St, Madison, WI, 53726",
 "2 Prospect Ave, Madison, WI, 53726",
 "14 N Prospect Ave, Madison, WI, 53726",
 "2115 Chadbourne Ave, Madison, WI, 53726",
 "2100 Van Hise Ave, Madison, WI, 53726",
 "109 N Prospect Ave, Madison, WI, 53726",
 "2001 Van Hise Ave, Madison, WI, 53726",
 "1926 Van Hise Ave, Madison, WI, 53726",
 "73 N Roby Rd, Madison, WI, 53726",
 "100 N Roby Rd, Madison, WI, 53726",
 "35 N Roby Rd, Madison, WI, 53726",
 "1 N Roby Rd, Madison, WI, 53726",
 "1846 Summit Ave, Madison, WI, 53726",
 "1850 Summit Ave, Madison, WI, 53726",
 "126 Forest St, Madison, WI, 53726",
 "2100 Chamberlein Ave, Madison, WI, 53726",
 "2024 Chamberlain Ave, Madison, WI, 53726",
 "2118 Chamberlain Ave, Madison, WI, 53726",
 "100 Bascom Pl, Madison, WI, 53726",
 "114 Bascom Pl, Madison, WI, 53726",
 "190 N Prospect Ave, Madison, WI, 53726",
 "168 N Prospect Ave, Madison, WI, 53726",
 "1717 Hoyt St, Madison, WI, 53726",
 "1615 Hoyt St, Madison, WI, 53726",
 "167 N Breese Terrace, Madison, WI, 53726",
 "35 N Breese Terrace, Madison, WI, 53726",
 "119 N Breese Terrace, Madison, WI, 53726",
 "101 N Allen St, Madison, WI, 53726",
 "102 N Allen St, Madison, WI, 53726",
 "103 N Allen St, Madison, WI, 53726",
 "104 N Allen St, Madison, WI, 53726",
 "105 N Allen St, Madison, WI, 53726",
 "2138 Chadbourne Ave, Madison, WI, 53726",
 "2134 Chadbourne Ave, Madison, WI, 53726",
 "2135 Chadbourne Ave, Madison, WI, 53726",
 "2136 Chadbourne Ave, Madison, WI, 53726",
 "2202 Regent Ave, Madison, WI, 53726",
 "2201 Regent Ave, Madison, WI, 53726",
 "2203 Regent Ave, Madison, WI, 53726",
 "2204 Regent Ave, Madison, WI, 53726"]



address_resource_fields = {
    'id': fields.Integer,
    'address_string': fields.String,
    'loc_lat': fields.Float,
    'loc_long': fields.Float
}

canvasser_resource_fields = {
    'addresses': fields.List(fields.Nested(address_resource_fields)),
    'distance': fields.Integer,
    'last_address_index': fields.Integer
}



class AddressListsRoute(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('addresses', action="append")
        args = parser.parse_args()
        addresses_json = args['addresses']
        addresses_json = test_addresses

        gm = Client('AIzaSyDAlFwslKhmuBMRjo1ZQ1o_xBWEx4vWx9I')
       #Build latitude/longitude list
        # addr_string_list = test_addresses #FOR TESTING ONLY
        # addr_geocode = gm.geocode(addr_string_list)
        addr_list = AddressList()
        db.session.add(addr_list)
        db.session.commit()

        for a in addresses_json:
            addr = Address()
            addr.address_string = a
            addr.loc_lat, addr.loc_long = gm.geocode(a)[0]["geometry"]["location"].values()
            addr.list_id = addr_list.id
            db.session.add(addr)

        db.session.commit()
        return

#class AddressListResource(Resource):


class MapRoute(Resource):
    @marshal_with(canvasser_resource_fields)
    def post(self, list_id):
        #Grab our stored list of addresses
        addr_list = AddressList.query.get(list_id)

        addresses = addr_list.addresses

        parser = reqparse.RequestParser()
        parser.add_argument('number of canvassers', type=int)
        parser.add_argument('canvasser number', type=int)
        args = parser.parse_args()

        num_users = args['number of canvassers']
        canv_num = args['canvasser number'] - 1

        matrix = create_matrix(addresses)
        start_houses = get_start_houses(matrix, num_users)
        canvassers = select_houses(matrix, start_houses, addresses)
        return canvassers[canv_num]
