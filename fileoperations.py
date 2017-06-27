# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:37:26 2017
@author: Anya

"""
import os
import io
from os import listdir
from os.path import isfile,join
from PIL import Image, ImageDraw
from dboperations import dboperations
import webbrowser
class fileoperations:
    def __init__(self):
        self.directory=''
        
    def list_images(self,directory=''):
        list_of_images=[] 
                
        if (directory.strip()==''):
            print('Please enter a valid directory')
            return list_of_images
        
        if (os.path.exists(directory)==False):
            print('Please enter a valid directory')
            return list_of_images
        
        filelist=[f for f in listdir(directory) if isfile(join(directory,f))]
        for file in filelist:
            filename, file_extension = os.path.splitext(join(directory,file))
            if file_extension.lower() in ['.jpg','.png','.jpeg']:
                list_of_images.append(file)
                
        return list_of_images
  
    def save_image_with_faces(self,folder,filename,faces):
        face_folder = join(folder,'faces')
        if not os.path.exists(face_folder):
           os.makedirs(face_folder)        
        
        im = Image.open(join(folder,filename))
        draw = ImageDraw.Draw(im)

        #define the square
        for face in faces:
            box = [(bound.x_coordinate, bound.y_coordinate)
                for bound in face.bounds.vertices]
            draw.line(box + [box[0]], width=5, fill='#00ff00')
    
        im.save(join(face_folder,filename))           
        
        
    def html_header(self):
        return '''<!DOCTYPE html>

                <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
                <head>
                    <meta charset="utf-8" />
                    <title>Picture information</title>
                    <style type="text/css">
                        .bx 
                        {
                            width: 400px;
                            padding: 10px;
                            height : 600px;
                            border: 1px solid #808080;
                            float: left;
                            margin-right: 10px;
                            overflow: hidden
                
                        }
                        .bx img { width: 100%}
                
                    </style>
                </head>
                <body>
                '''
    def html_footer(self):
        return '</body></html>'
        
   
        
        
    def save_to_html_file(self,filelist,folder):
        db = dboperations()
        image_html = ''
        for file in filelist:
            file_id = file[0]
            file_name = file[3]
            labels = db.retrieve_labels(file_id)
            label_html=''
            for lbl in labels:
                label_html +='\n{0:.1%} -> {1}<br />'.format(lbl[2],lbl[1]) 
                
            image_html += '''\n<div class="bx"><img src="{0}"/> <br /><h3>Picture Info</h3>
                            {1}\n
                            </div>\n
                            '''.format(file_name,label_html)
                            
        all_content = self.html_header() + image_html + self.html_footer()
        
        
        html_file = join(folder,'image_info.html')
        with io.open(html_file, "w") as fr:
            fr.write(all_content)

        webbrowser.open('file://' + os.path.realpath(html_file))
            