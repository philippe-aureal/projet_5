#! /usr/bin/env python3
# coding: utf-8
import requests
from packages.Api_util import Api as api
import json
import os
from packages.table import *
from packages.db_connect import DbConnect



class Off:

    def __init__(self):
        """"""
        self.api = api()
        self.db = DbConnect()
        self.Category = Category()
        self.Store = Store()


        # vérification du json
    def before_interaction(self):
        if self.api.verif_files() == False:

            self.api.data_processing(self.api.api_request())



    def supply_database(self):
        self.db.create_database()
        with open('datas/list.json','r') as f:
            datas = json.load(f)
        i=0
        for item in datas:

            #print(type(item))
            self.Category.insert(item)
            #cat_id = self.Category.get_id(item)
            self.Store.insert(item)
            i +=1
            print(i)




























"""    bd = DbConnect()
    print(bd.user)
    bd.connect()"""
