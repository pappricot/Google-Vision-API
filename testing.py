# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:46:02 2017

@author: Anya
"""

from dboperations import dboperations
db = dboperations()
folder = 'C:/Users/Anya/Desktop/pythonSpring/python-google-vision'
db.retrieve_files(folder)
# print(listfiles)
db.close_db()