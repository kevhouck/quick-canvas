from app import db


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_string = db.Column(db.String(200))
    loc_long = db.Column(db.Float)
    loc_lat = db.Column(db.Float)
    list_id = db.Column(db.Integer, db.ForeignKey('address_list.id'))

    def is_even_street_num(self):
        addr_num_s =  self.address_string.split(" ")
        addr_num = int(addr_num_s)
        num = addr_num % 10

        if num == 0 or num == 2 or num == 4 or num == 6 or num == 8:
            return True
        return False

