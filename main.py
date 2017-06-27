# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:35:53 2017

@author: Anya
"""
import io
import sys
import time
from google.cloud import vision
from fileoperations import fileoperations
from dboperations import dboperations


def get_files():
    folder = 'C:/Users/Anya/Desktop/pythonSpring/pics' #input('Please enter a directory for images to analyze : ')
    f = fileoperations()
    images = f.list_images(folder)
    if len(images)==0:
        print('No images found in :' + folder)
        sys.exit('Exiting..')
    return folder,images

def save_files(folder,images):
    db = dboperations()
    print('Saving images :')
    print(images)
    db.insert_files(folder,images)
    db.close_db()


def get_google_vision(folder):
    #connect to google cloud project
    vision_client = vision.Client(project='vision-python-1993')
    db = dboperations()
    f = fileoperations()
    filelist = db.retrieve_files(folder)
    print('Get files from database for folder : ' + folder)
    for file in filelist:
        file_id = file[0]
        full_file_name = file[1]
        file_name = file[3]
        print('Opening image ' + file_name + ' for analysis..')
        with io.open(full_file_name, 'rb') as image_file:
            content = image_file.read()
           # image = vision_client.image(content=content, )    
           # labels = image.detect_labels() 
           # time.sleep(5)
           # db.save_labels_fd(file_id,labels,0)
                 
            print('Saving the descriptions for the file..')
          
           
            
            
    db.close_db()
    f.save_to_html_file(filelist,folder)
    
    
    
    

def main():
    db = dboperations()
    db.create_tables()
    db.close_db()
    
    folder,images = get_files();
    save_files(folder,images);
    get_google_vision(folder)

if __name__ == '__main__':
    main()
    

