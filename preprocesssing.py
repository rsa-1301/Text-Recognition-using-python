import cv2
import numpy as np

img = cv2.imread('Skewed.jpg')
r = img.shape[0]
c = img.shape[1]
gray_img = np.zeros((r,c,1), np.uint8)
binary_img = np.zeros((r,c,1), np.uint8)
noise_img = np.zeros((r,c,1), np.uint8)
for i in range(0,r):
    for j in range(0,c):
        px = img[i,j]
        if ((px[0]>px[1]) and (px[0]>px[2])):
            m = px[0]
        elif (px[1]>px[2]):
            m = px[1]
        else:
            m = px[2]
        gray_img[i,j] = m

for i in range(0,r):
    for j in range(0,c):
        m = gray_img[i,j]
        if (m<120):
            binary_img[i,j] = 0 
        else:
            binary_img[i,j] = 255

for i in range(1,r-1):
    for j in range(1,c-1):
        if(binary_img[i,j]==0 and binary_img[i-1,j-1]==255 and binary_img[i-1,j]==255 and binary_img[i-1,j+1]==255 and binary_img[i,j-1]==255 and binary_img[i,j+1]==255 and binary_img[i+1,j-1]==255 and binary_img[i+1,j]==255 and binary_img[i+1,j+1]==255):
            noise_img[i,j]=255
        else:
            noise_img[i,j]=binary_img[i,j]

cv2.imwrite('images/Binary_Image.jpg',binary_img)
cv2.imwrite('images/NoiseLess_Image.jpg',noise_img)
cv2.imwrite('images/Gray_Image.jpg',gray_img)
cv2.imwrite('images/Original_image.jpg',img)

