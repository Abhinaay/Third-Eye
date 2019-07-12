#!/usr/bin/python3
# This liberary is used for image processing and editing there are a lot of inbuilt
# Functions which we can use to edit image contents and create new images
import cv2

# This is a class which contains functions for the image processing
class A():

    # The function imread is used to open an image from the system
    # It takes 1 argument as image source
    image = cv2.imread('/home/pykid/Desktop/index.jpeg')

    # This function is used to fill yellow color in the image
    def A_yellow(self):
        # We are using the copy function to make a copy of the block A
        # We are deducting Red color as such the mixture of Green and Red color is Yellow
        # As such we are deducting the remaining colors to get an image of yellow color
        blocka = self.image[400:637,575:800].copy() - [255,0,0]
        # Since when we replace an image we need to change its type unless 
        # it will cause disturbance in image
        blocka = blocka.astype('uint8')
        # Now we are replacing the custom image with the image we have designed
        self.image[400:637,575:800] = blocka
        # Now returning the image back to where the object is called
        return self.image

    # This function is used to fill Red color in the image
    def A_red(self):
        # We are using the copy function to make a copy of the block A
        # We are deducting Red color as such the mixture of Green and Red color is Yellow
        # As such we are deducting the remaining colors to get an image of yellow color
        blocka = self.image[400:637,575:800].copy() - [255,255,0]
        # Since when we replace an image we need to change its type unless 
        # it will cause disturbance in image
        blocka = blocka.astype('uint8')
        # Now we are replacing the custom image with the image we have designed
        self.image[400:637,575:800] = blocka
        # Now returning the image back to where the object is called
        return self.image

    # This function is used to fill Green color in the image
    def A_green(self):
        # We are using the copy function to make a copy of the block A
        # We are deducting Red color as such the mixture of Green and Red color is Yellow
        # As such we are deducting the remaining colors to get an image of yellow color
        blocka = self.image[400:637,575:800].copy() - [150,50,90]
        # Since when we replace an image we need to change its type unless 
        # it will cause disturbance in image
        blocka = blocka.astype('uint8')
        # Now we are replacing the custom image with the image we have designed
        self.image[400:637,575:800] = blocka
        # Now returning the image back to where the object is called
        return self.image

    # This function is used to fill Orange color in the image
    def A_orange(self):
        # We are using the copy function to make a copy of the block A
        # We are deducting Red color as such the mixture of Green and Red color is Yellow
        # As such we are deducting the remaining colors to get an image of yellow color
        blocka = self.image[400:637,575:800].copy() - [200,100,0]
        # Since when we replace an image we need to change its type unless 
        # it will cause disturbance in image
        blocka = blocka.astype('uint8')
        # Now we are replacing the custom image with the image we have designed
        self.image[400:637,575:800] = blocka
        # Now returning the image back to where the object is called
        return self.image

    # This function is used to fill brown color in the image
    def A_brown(self):
        # We are using the copy function to make a copy of the block A
        # We are deducting Red color as such the mixture of Green and Red color is Yellow
        # As such we are deducting the remaining colors to get an image of yellow color
        blocka = self.image[400:637,575:800].copy() - [150,100,60]
        # Since when we replace an image we need to change its type unless 
        # it will cause disturbance in image
        blocka = blocka.astype('uint8')
        # Now we are replacing the custom image with the image we have designed
        self.image[400:637,575:800] = blocka
        # Now returning the image back to where the object is called
        return self.image

'''
We have created a class named A which contains multiple functions defining colors for the map
This class is responsible for filling and modifying colors in the map to show the density.
The Functions are specifically designed to fill a particular color in the map.
'''
object1 = A()

# Asking user to input the value of number of people
x = int(input('bhar jaldi'))

# If the number of people in the image are in between 0 and 10 then these statements will execute
if 0<x < 10:
    # Calling the function to fill the green color in the map
    maps = object1.A_green()

    # cv2 library is used to display and modify images and this function imshow is used to
    # show the image 
    cv2.imshow('blocka',maps)

# If the number of people in the image are in between 10 and 20 then these statements will execute
elif 10<=x<20:
    # Calling the function to fill the Yellow color in the map
    maps = object1.A_yellow()

    # cv2 library is used to display and modify images and this function imshow is used to
    # show the image 
    cv2.imshow('blocka',maps)

# If the number of people in the image are in between 20 and 30 then these statements will execute
elif 20<=x<30:
    # Calling the function to fill the Orange color in the map
    maps = object1.A_orange()

    # cv2 library is used to display and modify images and this function imshow is used to
    # show the image 
    cv2.imshow('map',maps)

# If the number of people in the image are in between 30 and 40 then these statements will execute
elif 30<=x<40:
    # Calling the function to fill the brown color in the map    
    maps = object1.A_brown()

    # cv2 library is used to display and modify images and this function imshow is used to
    # show the image 
    cv2.imshow('map',maps)

# If the number of people in the image are more then 40 then these statements will execute
elif x >=40:
    # Calling the function to fill the Red color in the map
    maps = object1.A_red()

    # cv2 library is used to display and modify images and this function imshow is used to
    # show the image 
    cv2.imshow('map',maps)

# In case if we have a very bad situation and some error occured then nothing happens 
# its like exception handling using if else
else:
    print('kuch kaam ni aata tumhe')

# This is a function of cv2 liberary used to hold the window output until the used press a key
cv2.waitKey(0)

# This function is used to destroy the window output
cv2.destroyAllWindows()
