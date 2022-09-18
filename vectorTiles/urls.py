"""vectorTiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vectortileApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('openlayers', views.openlayerView.as_view(), name='openlayers'),
    path('leaflet', views.leafletView.as_view(), name='leaflet'),
    path('layers/district/<int:z>/<int:x>/<int:y>', views.DistrictTileView.as_view(), name="district-layer"),
]
