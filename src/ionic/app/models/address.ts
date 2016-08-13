
export class Address {
    public id:number;
    public address_string:string;
    public loc_lat:number;
    public loc_long:number;

    constructor() {

    }

    public static fromJSON(jsonObj): Address {
        var addr = new Address();
        addr.id = jsonObj['id'];
        addr.address_string = jsonObj['address_string'];
        addr.loc_lat = jsonObj['loc_lat'];
        addr.loc_long = jsonObj['loc_long'];
        return addr;
    }
}