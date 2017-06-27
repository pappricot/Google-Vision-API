import os

os.chdir('C:/Users/Anya/Desktop/pythonSpring/python-google-vision')

for filenames in os.walk('C:/Users/Anya/Desktop/pythonSpring/python-google-vision'):
    print('Files ', filenames)
    print()