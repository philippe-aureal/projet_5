#!/usr/bin/env python
# -*- coding: utf-8 -*-
from packages.db_connect import DbConnect

class Table:

    def __init__(self, fillables):
#       self.table = ""
        self.db = DbConnect()

    def insert(self):
        request = "Insert INTO " + self.table + " ("
        for key, val in self.fillables:
            request += key + ", "
            request += ") "
            request += "VALUES ("
            for key, val in self.fillables:
                request += val + ", "
                request += ")"
        return db_connect.execute_sql(request)

    def get_one(self):
        request = "SELECT * FROM " + self.table + " WHERE id = id"
        return db_connect.execute_sql(request)

    def get_all():
        request = "SELECT * FROM " + self.table
        return db_connect.execute_sql(request)
