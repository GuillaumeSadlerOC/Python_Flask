""" TestParser """

# -*- coding: utf-8 -*-
from gpbapp.scripts.parser import Parser


class TestParser():

    def setup(self):
        self.parser = Parser()

    def test_parser(self):
        """ Test if a Parser class is instantiated. """

        assert type(self.parser) == Parser

    def test_sentence_parsing(self):

        self.parser.sentence_parsing(sentence="Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")

        assert self.parser.request_keyword == {
            "status" : "FOUND",
            "greeting_form" : "TRUE",
            "sentence_type" : "TYPE TWO",
            "keyword" : "OpenClassrooms"
        }

    def sentence_parsing_rescue(self):

        self.parser.sentence_parsing_rescue(sentence="Salut GrandPy ! ... Est-ce que tu connais l'adresse d'OpenClassrooms?")

        assert self.parser.sentence == "openclassrooms"

    def test_sentence_empty(self):

        self.parser.sentence_parsing(sentence="")

        assert self.parser.request_keyword == {
            "status" : "EMPTY",
            "greeting_form" : "",
            "sentence_type" : "",
            "keyword" : ""
        }
