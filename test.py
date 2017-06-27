import os
import io
import sys
from google.cloud import vision
from PIL import Image, ImageDraw
from fileoperations import fileoperations


ask_directory = input('Please enter a directory for images to analyze : ')
f = fileoperations()
images = f.list_images(ask_directory)
if len(images)==0:
    print('No images found in :' + ask_directory)
    sys.exit('Exiting..')

#connect to google cloud project
vision_client = vision.Client(project='vision-python-1993')

# w
for x in images:
    file_name = os.path.join(ask_directory,x)
    print('Opening image : ' + x + ' for analysis..')
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = vision_client.image(
        content=content, )
    
    print('Detecting labels for the image : ' + x)
    labels = image.detect_labels()
    faces =image.detect_faces()
    for label in labels:
        print(label.score, label.description)

#save face detection in a square
    im = Image.open(file_name)
    draw = ImageDraw.Draw(im)

#define the square
    for face in faces:
        box = [(bound.x_coordinate, bound.y_coordinate)
            for bound in face.bounds.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')
    
    im.save('new.jpg')
    
#i need to remember what i said during presentation because i made them up during the speech

#yuowanted to use twitter sensetivity analysis?
#string?
#emoji???
    