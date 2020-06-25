""" TestGeocoder """

# -*- coding: utf-8 -*-
from gpbapp.scripts.geocoder import Geocoder
import json
import requests


class TestGeocoder():

    def setup(self):
        """ This method create an instance of Geocoder. """

        self.geocoder = Geocoder()

    def test_geocoder(self):
        """ This method test if the instance created is
            of type "Geocoder". """

        assert type(self.geocoder) == Geocoder

    def test_reverse_geocoding(self, monkeypatch):
        """ This method test the result from nominatim OpenStreetMap API.
            This method use a mock for emulate a request. """

        # JSON response from OpenStreetMap
        osm_response = {
            "place_id": "251835758",
            "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
            "osm_type": "node",
            "osm_id": "6242758322",
            "boundingbox": [
                "48.8747286",
                "48.8748286",
                "2.3504385",
                "2.3505385"
            ],
            "lat": "48.8747786",
            "lon": "2.3504885",
            "display_name": "OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10e, Paris, Île-de-France, France métropolitaine, 75010, France",
            "class": "office",
            "type": "company",
            "importance": 0.101,
            "address": {
                "address29": "OpenClassRooms",
                "house_number": "7",
                "road": "Cité Paradis",
                "suburb": "Quartier de la Porte-Saint-Denis",
                "city_district": "Paris 10e Arrondissement",
                "city": "Paris",
                "county": "Paris",
                "state": "Île-de-France",
                "country": "France",
                "postcode": "75010",
                "country_code": "fr"
            }
        }

        def mockreturn(request):
            return json.dumps(osm_response).encode()

        monkeypatch.setattr(requests, 'Response', mockreturn)

        assert self.geocoder.reverse_geocoding(keyword="OpenClassrooms") == {
            "status" : "FOUND",
            "display_name" : "OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10e, Paris, Île-de-France, France métropolitaine, 75010, France",
            "lat" : 48.8747786,
            "lon" : 2.3504885
        }
