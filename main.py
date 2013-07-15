# -*- coding: utf-8 -*-

class SynDictionary:
    def __init__(self):
        self.map = {}
        self.load()

    def load(self):
        "builds reverse index syn_word -> root_word from table root_word: sw1, sw2, ... swN"
        t = """POS пос
        АД декларация, алкаш
        обмен репликация
        """

        pass

    def get(self, word):
        """ returns root word or passed word if no root word found """

        if self.map.exist(word):
            return self.map[word]
        else:
            return word



class StopWordFilter:
    def filter(self, word):
        """returns either passed word or empty"""
        return word

class Tokenizer:
    pass

class MorphoFilter:
    def filter(self, word):
        pass


class Index:
    def __init__(self):
        pass

    def add(self, text_path, text_body):
        # calc text hash
        # if such hash found - ignore the text - because it is processed already
        pass


class Program:
    def __init__(self):
        self.index = Index()
        pass

    def help(self):
        pass

    def create(self, db_path):
        self.db_path = db_path
        self.create_folder(db_path)
        # TODO: create sqllite db
        pass

    def index(self, source_path):
        # loop over files in source folder
        # and index its content
        self.index.add(text_name, text_body)
        pass

    def source(self, top_word_count):
        # get top words and outputs relevant sources
        pass

    def list(self):
        pass

    def create_folder(self, path):
        pass


# ENTRY
p = Program()

# parse cmd line
# execute command

p.create("./db")
p.index("./source")

p.list()     #
p.source(10) # source top ten words