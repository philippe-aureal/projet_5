#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Product(Table):
    """ class defining a product characterized by:"""


    def __init__(self, fillables=None):
        self.table = "product"
        self.fillables = {
            'id' : None,
            'name_product' : None,
            'brand_product' : None,
            'nutritional_note' : None,
            'url' : None,
            'category_id' : None
            }
        """self.fill(fillables)"""
