import cv2 as cv
import numpy as np
import math

image=cv.imread('jigsaw.jpg')
# cv.imshow('Jigsaw', image)


#1st
cropped1=image[0:200, 0:190]
# cv.imshow('Jigsaw1', cropped1)


#2nd
cropped2=image[200:399, 0:189]
# cv2_imshow(cropped2)

# rotating cropped2 about center
def rotate(img, angle, rotPoint=None):
  (height,width)=img.shape[:2]
  if rotPoint is None:
    rotPoint=(width//2, height//2)

  rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
  dimensions=(width,height)
  return cv.warpAffine(img,rotMat,dimensions)

cropped2rot=rotate(cropped2, 180)
cropped2flip=cv.flip(cropped2rot, 1)
final2=cropped2flip[1:200, 0:189]
#Resizing for better smoothness
ff2=cv.resize(final2, (192, 208))
# cv.imshow('fi2',ff2)


#3rd
cropped3=image[150:330, 515:700]
# cv.imshow('f3',cropped3)

#Flipping cropped3 horizontally
cropped3flip=cv.flip(cropped3, 1)
# cv.imshow('ff3',cropped3flip)


#4th
cropped4=image[370:421, 370:797]
# cv.imshow('f4', cropped4)
cropped4flip=cv.flip(cropped4, 0)
# cv.imshow('ff4', cropped4flip)

image[150:330, 515:700]=cropped3flip
image[370:421, 370:797]=cropped4flip
image[200:400, 0:190]=cropped1
image[0:208, 0:192]=ff2

cv.imshow('Solved', image)
cv.imwrite('jigsolved.jpg', image)


cv.waitKey(0)
cv.destroyAllWindows()