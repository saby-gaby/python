import cv2     # pip install opencv-python

img = cv2.imread('image.jpg')

black_white_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #convert to black & gray

for i, pixel in enumerate(img[0]):   # po vertikal pyrviq red pixeli
    print(f'Pixel {i} --> {pixel}')
    print('* * * * * * * * * * * * *')

cv2.imshow('img', img)
cv2.waitKey(0)
