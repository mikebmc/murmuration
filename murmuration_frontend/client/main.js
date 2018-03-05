import { allHoods } from './allHoods';

//Meteor.subscribe('toplayer');

Meteor.startup(function() {
  $(window).resize(function() {
    $('#map').css('height', window.innerHeight - 127);
  });
  $(window).resize(); // trigger resize event
});

Template.map.rendered = function() {
	var mymap = L.map('map').setView([40.767520316999857, -73.904136377999933], 13);
	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
			attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
			maxZoom: 18,
			id: 'mapbox.streets',
			accessToken: 'pk.eyJ1IjoiZ2FobWVkODQwMyIsImEiOiJjamRqYTdrb3UwdnZrMnhzYWJ3MW54bzZoIn0._dnzXUrrS4XsO1LsEGPyFw'
	}).addTo(mymap);
	Meteor.call("get.neighborhoodColors", function(err, rawTopLayer){
		console.log("Getting Colors");
		var hoodColors = setHoodMap(rawTopLayer);
		addLayers(allHoods, mymap, hoodColors);
	});
};

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
      "weight": 5,
      "opacity": 0.8,
			"fillOpacity": 0.5
    };
    L.geoJSON(layer, {
        style: options
    }).addTo(mymap);
  }
}

function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
