from picamera import PiCamera
from time import sleep
from skimage.io import imread
import numpy as np
from skimage.transform import resize
from skimage.color import rgb2gray
from keras.models import load_model

camera = PiCamera(resolution=(1792,1792))
camera.start_preview()
sleep(10)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

im = imread("image.jpg")

# resize to 28 x 28
im_resize = resize(im,(28,28), mode='constant')

# turn the image from color to gray
im_gray = rgb2gray(im_resize)

# the color of the original set are inverted, so we invert it
hereim_gray_invert = 255 - im_gray*255

#treat color under threshold as black
im_gray_invert[im_gray_invert<=90] = 0

model=load_model('mnist_trained_model.h5')
im_final = im_gray_invert.reshape(1,28,28,1)

# the below output is a array of possibility of respective digit
ans = model.predict(im_final)
print(ans)

# choose the digit with greatest possibility as predicted dight
ans = ans[0].tolist().index(max(ans[0].tolist()))
print("the predicted digit is", ans)