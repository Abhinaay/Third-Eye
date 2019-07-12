#!/usr/bin/python3
import cv2 

class BlockA:
    def __init__(self,filename,count):
        image = cv2.imread(self.filename)
        self.count = count

