$(document).ready(function() {

var spatialView = new ol.View({
      // projection: projection,
      projection: 'EPSG:3857',
      center: ol.proj.transform([83.5295724, 27.8866973518], 'EPSG:4326', 'EPSG:3857'),
      zoom: 7
  });


var frontmap = new ol.Map({
      layers: layers,
      target: 'map',
      controls: ol.control.defaults({
          zoom: false,
          attribution: false,
          rotate: false
      }),
      view: spatialView
  });


});
