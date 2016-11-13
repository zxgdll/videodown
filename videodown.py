#!/bin/env python
# coding=utf-8
import requests
import urllib2
import re
from bs4 import BeautifulSoup


class Video(object):
    def __init__(self, name, url, score, link):
        self.name = name
        self.url = url
        self.score = score
        self.link = link

    def __str__(self):
        return '%s,\t%s 分,\t%s' % (self.name, self.score, self.link)
    __repr__ = __str__


def getSoup(url):
    page = requests.get(url)
    page.encoding = 'gb18030'
    return BeautifulSoup(page.text, 'html.parser')


def filtervideo(url):
    resultList = []
    soup = getSoup(url)
    tables = soup.find_all('table', class_="tbspan")
    for table in tables:
        nameA = table.find('td',)
