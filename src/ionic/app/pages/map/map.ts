declare var google:any;
declare var MarkerWithLabel:any;

import {Page, NavController, NavParams} from 'ionic-angular';
import {Http, Headers} from 'angular2/http';
import {Address} from '../../models/address'
import {Observable} from 'rxjs/Observable'

@Page({
    templateUrl: 'build/pages/map/map.html',
})

export class MapPage {

    addresses:Array<Address>;
    map:any;

    constructor(private navParams: NavParams){
        this.addresses = navParams.get('addresses');
    }

    ngAfterViewInit() {
        this.loadMap()
    }

    loadMap() {
        // google will work still even though it cant find it
        var first_address = this.addresses[0];
        let latLng = new google.maps.LatLng(first_address.loc_lat, first_address.loc_long);

        let mapOptions = {
            center: latLng,
            zoom: 15,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        this.map = new google.maps.Map(document.getElementById("map"), mapOptions);

        var markers = Array<any>();

        for(var i = 0; i < this.addresses.length; i++) {
            let latLng = new google.maps.LatLng(this.addresses[i].loc_lat, this.addresses[i].loc_long);

            /**let marker = new google.maps.Marker({
                map: this.map,
                animation: google.maps.Animation.DROP,
                position: latLng,
                label:  ((i % 9) + 1).toString()
            });*/

            var marker = new MarkerWithLabel({
                position: latLng,
                map: this.map,
                draggable: false,
                raiseOnDrag: false,
                labelContent: (i + 1).toString(),
                labelAnchor: new google.maps.Point(15, 65),
                labelClass: "labels", // the CSS class for the label
                labelInBackground: false,
                icon: this.pinSymbol()
            });
            markers.push(markers)
        }
    }
    pinSymbol(color) {
    return {
        path: 'M 0,0 C -2,-20 -10,-22 -10,-30 A 10,10 0 1,1 10,-30 C 10,-22 2,-20 0,0 z',
        fillColor: '#ffdddd',
        fillOpacity: 1,
        strokeColor: '#000',
        strokeWeight: 2,
        scale: 2
    };
}
}