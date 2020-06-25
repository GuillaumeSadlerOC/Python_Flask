""" TestGeoSearcher """

# -*- coding: utf-8 -*-
from gpbapp.scripts.geosearcher import GeoSearcher
import json
import requests

class TestGeoSearcher():

    def setup(self):
        """ This method create an instance of GeoSearcher. """

        self.geosearcher = GeoSearcher()

    def test_geosearcher(self):
        """ This method test if the instance created is
            of type "GeoSearcher". """

        assert type(self.geosearcher) == GeoSearcher

    def test_get_address_story(self, monkeypatch):
        """ This method test the result from Media Wiki API.
            This method use a mock for emulate a request. """

        # JSON response from Media Wiki API
        mw_response = {
            "batchcomplete": "",
            "query": {
                "pages": {
                    "438469": {
                        "pageid": 438469,
                        "ns": 0,
                        "title": "Rue d'Hauteville",
                        "index": 0,
                        "extract": "La rue d’Hauteville est une voie publique située dans le 10e arrondissement de Paris."
                    },
                    "5091748": {
                        "pageid": 5091748,
                        "ns": 0,
                        "title": "Hôtel Bourrienne",
                        "index": 1,
                        "extract": "L'Hôtel Bourrienne (appelé aussi Hôtel de Bourrienne et Petit Hôtel Bourrienne) est un hôtel particulier du XVIIIe siècle situé au 58 rue d'Hauteville dans le 10e arrondissement de Paris. Propriété privée, il est classé au titre des monuments historiques depuis le 20 juin 1927."
                    },
                    "5653202": {
                        "pageid": 5653202,
                        "ns": 0,
                        "title": "Cité Paradis",
                        "index": 2,
                        "extract": "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris."
                    },
                    "6035646": {
                        "pageid": 6035646,
                        "ns": 0,
                        "title": "Hôtel Botterel de Quintin",
                        "index": 3,
                        "extract": "L'Hôtel de Botterel-Quintin d’Aumont est un des principaux vestiges de l'âge d’or du quartier Poissonnière, dans le 10e arrondissement de Paris."
                    }
                }
            }
        }

        def mockreturn(request):
            return json.dumps(mw_response).encode()

        monkeypatch.setattr(requests, 'Response', mockreturn)

        assert self.geosearcher.get_address_story(lat=48.8747786, lon=2.3504885) == {
            "status" : "FOUND",
            "title" : "Rue d'Hauteville",
            "extract" : "La rue d’Hauteville est une voie publique située dans le 10e arrondissement de Paris."
        }