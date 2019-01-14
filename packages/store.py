#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Store(Table):
    """ class defining a Store characterized by:"""


    def __init__(self, fillables=None):
        self.table = "store"
        self.fillables = {
            'id' = None,
            'name_store' : None

            }
        """self.fill(fillables)"""
