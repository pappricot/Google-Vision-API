# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:51:54 2017

@author: Anya
"""
import sqlite3
from os.path import join

class dboperations:
    def __init__(self,dbfile='imageDatabase10.db'):
        self.connection = sqlite3.connect(dbfile)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('''Create table if not exists imageFiles 
                              (fid INTEGER PRIMARY KEY AUTOINCREMENT,
                              fullPath TEXT UNIQUE,
                              folder TEXT, fileName TEXT,
                              faceDetect INTEGER
                              )''')
        
        self.cursor.execute('''Create table if not exists labelScores 
                              (fid INTEGER,
                              label TEXT, 
                              score REAL)''')
        
    def insert_files(self,folder,filenamelist):
        for f in filenamelist:
            self.cursor.execute('''INSERT OR IGNORE INTO imageFiles 
                                   (fullPath,folder,fileName,faceDetect) 
                                   VALUES (?,?,?,?)''',
                                   (join(folder,f),folder,f,0)
                                   )
        self.connection.commit()
        
    def save_labels_fd(self,fid,labels,facedetect):
        for label in labels:
            self.cursor.execute('''INSERT OR IGNORE INTO labelScores 
                                   (fid,label,score) 
                                   VALUES (?,?,?)''',
                                   (fid,label.description,label.score)
                                   )
            self.cursor.execute('''UPDATE imageFiles SET faceDetect= ?
                                   WHERE fid = ?''',
                                   (facedetect,fid))
            
        self.connection.commit()
            
    def retrieve_files(self,folder):
        sql = "SELECT * FROM imageFiles WHERE folder='{0}'".format(folder)
        self.cursor.execute(sql) 
        all_rows= self.cursor.fetchall()                               
        return all_rows         

    def retrieve_labels(self,fid):
        sql = "SELECT * FROM labelScores WHERE fid={0}".format(fid)
        self.cursor.execute(sql) 
        all_rows= self.cursor.fetchall()                               
        return all_rows         
    
    def close_db(self):
        self.connection.close()
        