#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import os
from os import path
import copy




list_products = []
dict ={}
products = {}

class Api:
    def __init__(self):
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.querystring = {"action":"process","tagtype_0":"categories",
                            "tag_contains_0":"contains",
                            "tag_0":"",
                            "page_size":"500","sort_by":"unique_scans_n",
                            "json":"1"}
        self.headers = {
            'cache-control': "no-cache",
            'Postman-Token': "354050b8-d327-4d4c-aebf-4737341ac849"
            }
        self.category = ("plats-prepares-surgeles","boissons-aux-fruits",
                         "cereales-pour-petit-dejeuner", "sandwichs", "yaourts-aux-fruits")
        self.list_products = []

    def api_request(self):
        """ create the request according to the category requested"""

        print("download API data........")
        for item in self.category:
            self.querystring['tag_0'] = item
            response = requests.request("GET", self.url, headers= self.headers,
                            params=self.querystring)
            self.dict = response.json()
            self.products = self.dict["products"]

            for element in self.products:
                element['categories'] = item
                self.list_products.append(element)
        return self.list_products


    def data_processing(self, list):

        for dictio in list:
            if ('nutrition_grade_fr' or 'brands' or 'product_name' or
                'url' or 'stores') not in dictio:
                del dictio
        with open('datas/list.json','w') as f:
            f.write(json.dumps(list, indent=4))

    def verif_files(self):
        self.json = os.path.exists('datas/list.json')
        return self.json
