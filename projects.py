#!/usr/bin/python3
# importing cv2 library for image processing
import cv2
import reciever_module as r
# class which represent the specific block covered by a camera
class A():

    # it is to read the image map
    image = cv2.imread('/home/pykid/Desktop/index.jpeg')
    
    #function for yellow color image range 10 to 20
    def A_yellow(self):
        blocka = self.image[400:637,575:800].copy() - [255,0,0]
        blocka = blocka.astype('uint8')
        img = self.image.copy()
        img[400:637,575:800] = blocka
        return img

    # function red color image range 40 above that is max
    def A_red(self):
        blocka = self.image[400:637,575:800].copy() - [255,255,0]
        blocka = blocka.astype('uint8')
        img = self.image.copy()
        img[400:637,575:800] = blocka
        return img

    # function for minimum no of people that is i range 1 to 10
    def A_green(self):
        blocka = self.image[400:637,575:800].copy() - [150,50,90]
        blocka = blocka.astype('uint8')
        img = self.image.copy()
        img[400:637,575:800] = blocka
        return img

    # function for people in range of 20 to 30
    def A_orange(self):
        blocka = self.image[400:637,575:800].copy() - [200,100,0]
        blocka = blocka.astype('uint8')
        img = self.image.copy()
        img[400:637,575:800] = blocka
        return img

    # function for crowd in range of 30 to 40
    def A_brown(self):
        blocka = self.image[400:637,575:800].copy() - [150,100,60]
        blocka = blocka.astype('uint8')
        img = self.image.copy()
        img[400:637,575:800] = blocka
        return img


# This loop will run infinitely
while True:
    objects = A()
    x = r.reciever("192.168.10.212",4444) 
    x = int(x)
    print(x)
    if 0< x < 3:
        # Color will change to green
        maps = objects.A_green()
        cv2.imwrite('image.jpeg',maps)
    elif 3<= x <6:
        # Color will change to Yellow
        maps = objects.A_yellow()
        cv2.imwrite('image.jpeg',maps)
    elif 6<= x <9:
        # Color will change to Orange
        maps = objects.A_orange()
        cv2.imwrite('image.jpeg',maps)
    elif 9<= x <12:
        #Color will change to Brown
        maps = objects.A_brown()
        cv2.imwrite('image.jpeg',maps)
    elif x >=12:
        # Highest Color will change to red
        maps = objects.A_red()
        cv2.imwrite('image.jpeg',maps)
    else:
        print('kuch kaam ni aata tumhe')
