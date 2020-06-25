""" Geocoder """

# -*- coding: utf-8 -*-
import requests, json


class Geocoder():
    def __init__(self):
        """ keyword (str ): keyword for reverse geocoding.
            address (dict): Result of reverse_geocoding. """

        self.keyword = None
        self.address = None

    def reverse_geocoding(self, keyword=None):
        """ Ask Open Street Map Nominatim API.
            Reverse geocoding (Search data OSM with keyword). """

        self.keyword = keyword
        self.address = {
            "status" : "",
            "lat" : 0,
            "lon" : 0,
            "display_name" : ""
        }

        try:

            url = "https://nominatim.openstreetmap.org/search.php"

            params = {
                'q' : self.keyword,
                'format' : 'json',
                'addressdetails' : '[0|1]'
            }

            r = requests.get(url=url, params=params)
            data = r.json()

            self.address["lat"] = float(data[0]["lat"])
            self.address["lon"] = float(data[0]["lon"])
            self.address["display_name"] = data[0]["display_name"]
            self.address["status"] = "FOUND"

        except:

            self.address["status"] = "NOT FOUND"

        return self.address
