#!/usr/bin/env python
# -*- coding: utf-8 -*-
from packages.db_connect import DbConnect

class Table:

    def __init__(self):
        self.table = ""
        self.db = DbConnect()
    def get_one(id):
        request = "SELECT * FROM " + self.table + " WHERE id = id"
        return db_connect.execute_sql(request)
    def get_all():
        request = "SELECT * FROM " + self.table
        return db_connect.execute_sql(request)
    def get_id():
        request = "SELECT id FROM " + self.table
        return db_connect.execute_sql(request)





class Product(Table):
    def __init__(self):
        self.table = "product"
    def insert(self, list):
        request = "INSERT INTO Product (name_product, brand_product, nutritional_note, url, category_id) VALUES (%s, %s, %s, %s, %s)", (list['product_name'], list['brands'], list['nutrition_grade_fr'], list['url'], cat_id)
        return db_connect.execute_sql(request)


class Category(Table):

    def __init__(self):
        self.table = "category"
        Table.__init__(self)
    def insert(self, item):
        request ="INSERT IGNORE INTO Category (name_category) VALUES (%s)"
        #print(type(request))

        return self.db.execute_sql(sql = request, data = (item['categories'],))


class Store(Table):
    def __init__(self):
        """"""
        self.table = "store"
        Table.__init__(self)
    def insert(self, item):
        request = "INSERT IGNORE INTO Store (name_store) VALUES (%s)"
        return self.db.execute_sql(sql = request, data = (item['stores'],))

class ProductStore(Table):
    def __init__(self):
        self.table = "product_store"
    def insert(self, prod_id, store_id):
        request = "INSERT IGNORE INTO Product_Store (store_product_id, store_id) VALUES (%s, %s)", (prod_id, store_id)
        return db_connect.execute_sql(request)

class Substitute(Table):
    def __init__(self):
        self.table = "substitute"
