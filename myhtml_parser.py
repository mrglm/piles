#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'FIL - Faculté des Sciences et Technologies -  Univ. Lille <http://portail.fil.univ-lille1.fr>_'
__date_creation__ = 'Mon Oct  7 16:39:07 2019'
__doc__ = """
:mod:`html_verif` module
:author: {:s}
:creation date: {:s}
:last revision:

""".format(__author__, __date_creation__)


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    """
    a class that parse a document and allow tag access
    :exemples:

    >>> parser = MyHTMLParser("<!DOCTYPE hml><html lang="fr"></html>")
    >>> parser.has_tag()
    True
    >>> parser.next_tag()
    '<html>'
    >>> parser.next_tag()
    '</html>'
    >>> parser.has_tag()
    False
    """
    def __init__(self, data):
        """
        constructor for MyHTMLParse
        :param data: (str) html document
        :UC: None
        """
        super().__init__()
        self.__tags = []
        self.__tag_index = 0
        HTMLParser.feed(self, data)


    def handle_starttag(self, tag, attrs):
        """
        handle an opening tag
        :param tag: (str) the opening tag
        :param attrs: (list) attributes
        """
        self.__tags.append('<{:s}>'.format(tag))


    def handle_endtag(self, tag):
        """
        handle an ending tag
        :param tag: (str) the ending tag
        """
        self.__tags.append('</{:s}>'.format(tag))


    def has_tag(self):
        """
        :return: (bool) True if document contains another tag, False otherwise
        """
        return self.__tag_index < len(self.__tags)


    def next_tag(self):
        """
        :return: (str) the next tag in document
        """
        res = self.__tags[self.__tag_index]
        self.__tag_index += 1
        return res


def html_to_str(fname):
    """
    Transforms a html file into a string
    :param fname: (str) The path to a file
    """
    with open(fname) as f:
        lines = f.readlines()
    return "".join([line.strip().replace("\n", "") for line in lines])


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
