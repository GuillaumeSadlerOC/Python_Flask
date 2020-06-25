""" Geosearcher """

# -*- coding: utf-8 -*-
import requests, json


class GeoSearcher():
    def __init__(self):
        """ lat           (float): latitude coordonate.
            lon           (float): longitude coordonate.
            address_story (dict ): result of get_address_story. """

        self.lat = None
        self.lon = None
        self.address_story = None

    def get_address_story(self, lat=None, lon=None):
        """ Ask Media Wiki API.
            Search data to keywords. """

        self.lat = lat
        self.lon = lon
        self.address_story = {
            "status" : "",
            "title" : "",
            "extract" : ""
        }

        try:
            url = "https://fr.wikipedia.org/w/api.php"

            params = {
                'action' : 'query',
                'prop' : 'extracts',
                'exintro' : '',
                'explaintext' : '',
                'exsentences' : '2',
                'generator' : "geosearch",
                'ggscoord' : "{}|{}".format(str(self.lat), str(self.lon)),
                'ggsradius' : "100",
                'format' : 'json'
            }

            r = requests.get(url=url, params=params)
            data = r.json()

            first_result = list(data["query"]["pages"])

            self.address_story["status"] = "FOUND"
            self.address_story["title"] = data["query"]["pages"][first_result[0]]["title"]
            self.address_story["extract"] = data["query"]["pages"][first_result[0]]["extract"]

        except:

            self.address_story["status"] = "NOT FOUND"

        return self.address_story