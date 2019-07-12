#!/usr/bin/python3
import cv2
class A():

    image = cv2.imread('/home/pykid/Desktop/index.jpeg')

    def A_yellow(self):
        blocka = self.image[400:637,575:800].copy() - [255,0,0]
        blocka = blocka.astype('uint8')
        self.image[400:637,575:800] = blocka
        return self.image

    def A_red(self):
        blocka = self.image[400:637,575:800].copy() - [255,255,0]
        blocka = blocka.astype('uint8')
        self.image[400:637,575:800] = blocka
        return self.image

    def A_green(self):
        blocka = self.image[400:637,575:800].copy() - [150,50,90]
        blocka = blocka.astype('uint8')
        self.image[400:637,575:800] = blocka
        return self.image

    def A_orange(self):
        blocka = self.image[400:637,575:800].copy() - [200,100,0]
        blocka = blocka.astype('uint8')
        self.image[400:637,575:800] = blocka
        return self.image

    def A_brown(self):
        blocka = self.image[400:637,575:800].copy() - [150,100,60]
        blocka = blocka.astype('uint8')
        self.image[400:637,575:800] = blocka
        return self.image


object1 = A()
x = int(input('bhar jaldi'))
if 0<x < 10:
    maps = object1.A_green()
    cv2.imshow('blocka',maps)
elif 10<=x<20:
    maps = object1.A_yellow()
    cv2.imshow('blocka',maps)
elif 20<=x<30:
    maps = object1.A_orange()
    cv2.imshow('map',maps)
elif 30<=x<40:
    maps = object1.A_brown()
    cv2.imshow('map',maps)
elif x >=40:
    maps = object1.A_red()
    cv2.imshow('map',maps)
else:
    print('kuch kaam ni aata tumhe')

cv2.waitKey(0)
cv2.destroyAllWindows()
