import {Page, NavController} from 'ionic-angular';
import {Http, Headers} from 'angular2/http';
import {Address} from '../../models/address'
import {Observable} from 'rxjs/Observable';
import {MapPage} from '../map/map';
import 'rxjs/add/operator/map';


@Page({
    templateUrl: 'build/pages/select_path/select_path.html',
})

export class SelectPathPage {
    list_id:number;
    num_canvassers:number;
    canvasser_num:number;

    constructor(
        private nav:NavController,
        private http:Http
    ) {
        this.list_id = 1;
        this.num_canvassers = 2;
        this.canvasser_num = 1;
    }

    submit() {
        let headers = new Headers();
        var url:string = 'http://localhost:5000/api/list/' + this.list_id + '/map';
        headers.append('Content-Type','application/json');
        var body = {};
        body['number of canvassers'] = this.num_canvassers;
        body['canvasser number'] = this.canvasser_num;
        this.http.post(url, JSON.stringify(body), {headers:headers})
        .map(res => res.json())
        .subscribe(json => {
                var addresses = new Array<Address>();
                for(var i = 0; i < json.addresses.length; i++) {
                    addresses.push(Address.fromJSON(json.addresses[i]))
                }
                console.log(addresses);
                this.nav.push(MapPage, {
                    addresses: addresses
                });
            }, err => console.log(err))
    }
}