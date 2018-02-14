import { allHoods } from './allHoods';
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
	addLayers(allHoods, mymap);
};
function addLayers(allLayers, mymap){
  for (var i = 0, len = allLayers['features'].length; i < len; i++) {
    var layer = allLayers['features'][i];
    var options = {
      "color": getRandomColor(),
      "weight": 5,
      "opacity": 0.65
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
