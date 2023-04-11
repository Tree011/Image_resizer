import cv2

image = cv2.imread('naruto.jpg')
#cv2.imshow('naruto.jpg',image)

#percentage by which the image is to be resized.

scale = 80

# change the dimensions:-

height = int(image.shape[0]*scale/100)
width = int(image.shape[1]*scale/100)

output = cv2.resize(image,(height,width))
cv2.imwrite('newimage.jpg',output)

cv2.waitKey(0)
cv2.destroyAllWindows()
