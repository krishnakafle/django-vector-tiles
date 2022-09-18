from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.
from django.views.generic import ListView
from vectortiles.postgis.views import MVTView
from vectortileApp.models import District


class DistrictTileView(MVTView, ListView):
    model = District
    vector_tile_layer_name = "districts"  # name for data layer in vector tile
    vector_tile_fields = ('district',)  # model fields or queryset annotates to include in tile
    vector_tile_geom_name = "geom"  # geom field to consider in qs


class openlayerView(TemplateView):
    template_name = 'openlayers.html'

class leafletView(TemplateView):
    template_name = 'leaflet.html'
