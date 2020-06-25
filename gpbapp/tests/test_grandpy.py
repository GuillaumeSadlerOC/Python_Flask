""" GrandPy test """

# -*- coding: utf-8 -*-
from gpbapp.scripts.grandpy import GrandPy


class TestGrandPy():

    def setup(self):
        """ This method create an instance of GrandPy. """

        self.grandpy = GrandPy()

    def test_grandpy(self):
        """ This method test if the instance created is
            of type "GrandPy". """

        assert type(self.grandpy) == GrandPy

    def test_sentence_type_3(self):
        """ Test if the method work. """

        self.grandpy.get_response(sentence="Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")

        assert self.grandpy.keyword == {
            "status" : "FOUND",
            "greeting_form" : "TRUE",
            "sentence_type" : "TYPE TWO",
            "keyword" : "OpenClassrooms"
        }

        assert self.grandpy.address == {
            "status" : "FOUND",
            "display_name" : "OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10e, Paris, Île-de-France, France métropolitaine, 75010, France",
            "lat" : 48.8747786,
            "lon" : 2.3504885
        }

        assert self.grandpy.address_story == {
            "status" : "FOUND",
            "title" : "Rue d'Hauteville",
            "extract" : "La rue d’Hauteville est une voie publique située dans le 10e arrondissement de Paris."
        }

    def test_sentence_type_2(self):
        """ Test if the method work. """

        self.grandpy.get_response(sentence="Salut GrandPy ! Connais-tu l'adresse d'OpenClassrooms ?")

        assert self.grandpy.keyword == {
            "status" : "FOUND",
            "greeting_form" : "TRUE",
            "sentence_type" : "TYPE THREE",
            "keyword" : "OpenClassrooms"
        }

        assert self.grandpy.address == {
            "status" : "FOUND",
            "display_name" : "OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10e, Paris, Île-de-France, France métropolitaine, 75010, France",
            "lat" : 48.8747786,
            "lon" : 2.3504885
        }

        assert self.grandpy.address_story == {
            "status" : "FOUND",
            "title" : "Rue d'Hauteville",
            "extract" : "La rue d’Hauteville est une voie publique située dans le 10e arrondissement de Paris."
        }

    def test_sentence_type_1(self):
        """ Test if the method work. """

        self.grandpy.get_response(sentence="Salut GrandPy ! Tu connais l'adresse d'OpenClassrooms ?")

        assert self.grandpy.keyword == {
            "status" : "FOUND",
            "greeting_form" : "TRUE",
            "sentence_type" : "TYPE ONE",
            "keyword" : "OpenClassrooms"
        }

        assert self.grandpy.address == {
            "status" : "FOUND",
            "display_name" : "OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10e, Paris, Île-de-France, France métropolitaine, 75010, France",
            "lat" : 48.8747786,
            "lon" : 2.3504885
        }

        assert self.grandpy.address_story == {
            "status" : "FOUND",
            "title" : "Rue d'Hauteville",
            "extract" : "La rue d’Hauteville est une voie publique située dans le 10e arrondissement de Paris."
        }

    def test_sentence_empty(self):
        """ Test if the method work. """

        self.grandpy.get_response(sentence="")

        assert self.grandpy.keyword == {
            "status" : "EMPTY",
            "greeting_form" : "",
            "sentence_type" : "",
            "keyword" : ""
        }

        assert self.grandpy.address == {
            "status" : "",
            "display_name" : "",
            "lat" : 0,
            "lon" : 0
        }

        assert self.grandpy.address_story == {
            "status" : "",
            "title" : "",
            "extract" : ""
        }
