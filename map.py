#!/usr/bin/python3
import cv2 

# Class Created named Block A
class BlockA:
    def __init__(self,filename,count):
        # This function is used to read the image from system
        image = cv2.imread(self.filename)
        self.count = count

