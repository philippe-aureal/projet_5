#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Category(Table):

    def __init__(self,fillables=None):
        self.table = "category"
        self.fillable = {
            'id' : None,
            'name_category' : None
        }
        self.fill(fillables)
