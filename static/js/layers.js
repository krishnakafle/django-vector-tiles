var osmLayer = new ol.layer.Tile({
    visible: true,
    zIndex: -2,
    source: new ol.source.OSM()

});

var districtLayer = new ol.layer.VectorTile({
    id: 'district',
    title: 'District',
    visible: true,
    declutter: true,
    source: new ol.source.VectorTile({
        tileGrid: ol.tilegrid.createXYZ({
            maxZoom: 24
        }),
        format: new ol.format.MVT(),
        url: '/layers/district/{z}/{x}/{y}'
    }),
    style: new ol.style.Style({
        stroke: new ol.style.Stroke({
            width: 2,
            color: '#FF7F7F'
        })
    })
});


var layers = [osmLayer, districtLayer]
