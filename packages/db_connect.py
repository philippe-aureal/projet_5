#! /usr/bin/env python3
# coding: utf-8
from os import path, name
import configparser
from packages import config
import mysql.connector
from mysql.connector import errorcode


class DbConnect:
    """class that allows connection to the database"""


    def __init__(self):

        self.host = config.host
        self.user = config.user
        self.password = config.password
        self.database = config.database
        #self.bdd = mysql.connector.connect()
        self.curA=self.connect()

    def connect(self):
        """connection methode to the database"""
        try:
            self.bdd = mysql.connector.connect(host = self.host,user = self.user,
                                                password = self.password, database = self.database )
            return self.bdd.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.bdd = mysql.connector.connect(host = self.host,user = self.user,
                                                    password = self.password)

                return self.bdd.cursor()

    def create_database(self):
        for line in open('database/create_database.sql').read().split(';\n'):
            self.curA.execute(line)







    def execute_sql(self, sql, data):
        self.curA.execute(sql, data)
        self.bdd.commit()
