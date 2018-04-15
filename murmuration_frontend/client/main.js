import { allHoods } from './allHoods';

Meteor.startup(function() {
  $(window).resize(function() {
    $('#map').css('height', window.innerHeight - 30);
  });
  $(window).resize(); // trigger resize event
	_.extend(Notifications.defaultOptions, {
        timeout: 10000
	});
});

Template.map.rendered = function() {
	var mymap = L.map('map', {
		center: [40.725353,-73.996382],
		zoom: 13,
		maxBounds: [[40.439149, -73.733989], [41.104299, -74.299827]],
		zoomControl: false,
	});

	L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png', {
			attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
			maxZoom: 19,
			id: 'mapbox.streets',
			accessToken: 'pk.eyJ1IjoiZ2FobWVkODQwMyIsImEiOiJjamRqYTdrb3UwdnZrMnhzYWJ3MW54bzZoIn0._dnzXUrrS4XsO1LsEGPyFw'
	}).addTo(mymap);
	Meteor.call("get.neighborhoodColors", function(err, rawTopLayer){
		var hoodColors = setHoodMap(rawTopLayer);
		addLayers(allHoods, mymap, hoodColors);
	});
	locateOnMap(mymap);
};

function locateOnMap(mymap) {
	mymap.locate({
		setView: true,
		watch: true,
		maxZoom: 14
	});
	
	//set some parameters for the location icon
	var myIcon = L.icon({
		iconUrl: '/images/map_icon.png',
		iconSize:     [14, 14],
		iconAnchor:   [7, 7],
	});

	mapMarker = L.marker([40.725353,-73.996382], {icon: myIcon}).addTo(mymap).setOpacity(0);

	mymap.on('locationfound', onLocationFound);
	mymap.on('locationerror', onLocationError);

}
function onLocationFound(e) {
	console.log('hey');
	mapMarker.setLatLng(e.latlng).setOpacity(1);
}

function onLocationError(e) {
	console.log('no way');
	var locationError = Notifications.info('Error', e.message);
}

function setHoodMap(rawTopLayer){
    var hoodColors = new Map();
    try{
      var hoodIds = rawTopLayer[0]['n_id'];
      var colors = rawTopLayer[0]['color'];
      var i = 0;
      for (i = 0; i < hoodIds.length; i++){
        hoodColors.set(hoodIds[i], colors[i]);
      }
      return hoodColors;
    }catch(e){
      throw new Meteor.Error("Error getting neighborhood colors (wee woo wee woo): " + e);
    }
    return null;
}

function addLayers(allLayers, mymap, hoodColors){
  for (var i = 0, len = allLayers['features'].length; i < len; i++) {
    var layer = allLayers['features'][i];
		var n_id = layer['properties']['LocationID'];
		var hoodColor = null;
		if (hoodColors.has(n_id)) hoodColor = hoodColors.get(n_id);
		var options = {
      "color": hoodColor,
			"id": n_id,
      "weight": 3,
      "opacity": 0.5,
			"fillOpacity": 0.6
    };
    L.geoJSON(layer, {
        style: options
    }).addTo(mymap);
  }
}
