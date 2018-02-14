Meteor.startup(function() {
  $(window).resize(function() {
    $('#map').css('height', window.innerHeight - 127);
  });
  $(window).resize(); // trigger resize event
});

Template.map.rendered = function() {
  L.Icon.Default.imagePath = '/meteor-leaflet/images/';

  var map = L.map('map', {
    doubleClickZoom: false
  }).setView([40.718068, -73.972955], 13.5);

  L.tileLayer.provider('OpenMapSurfer.Roads').addTo(map);
};
