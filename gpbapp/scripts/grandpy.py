""" GrandPy """

# -*- coding: utf-8 -*-
from gpbapp.scripts.geocoder import Geocoder
from gpbapp.scripts.geosearcher import GeoSearcher
from gpbapp.scripts.parser import Parser


class GrandPy():
    def __init__(self):
        """ keyword       (str ): result of sentence_parsing.
            address       (dict): result of reverse_geocoding.
            address_story (dict): result of get_address_story.
            parser        (obj ): instance of Parser.
            geocoder      (obj ): instance of Geocoder.
            geosearcher   (obj ): instance of GeoSearcher. """

        self.keyword = {
            "status" : "",
            "greeting_form" : "",
            "sentence_type" : "",
            "keyword" : ""
        }
        self.address = {
            "status" : "",
            "display_name" : "",
            "lat" : 0,
            "lon" : 0
        }
        self.address_story = {
            "status" : "",
            "title" : "",
            "extract" : ""
        }
        self.parser = Parser()
        self.geocoder = Geocoder()
        self.geosearcher = GeoSearcher()

    def get_response(self, sentence=None):
        """ Gathers the functions that allow the application ro
            respond to what is asket of it. """

        #1. Parsing
        self.keyword = self.parser.sentence_parsing(sentence=sentence)

        if self.keyword["status"] == "FOUND":
            #2. Geocoding
            self.address = self.geocoder.reverse_geocoding(keyword=self.keyword["keyword"])

            #3. Geosearching
            self.address_story = self.geosearcher.get_address_story(lat=self.address["lat"], lon=self.address["lon"])
