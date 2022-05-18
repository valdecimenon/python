

#pip install opencv-python

from skimage import io
import cv2

imagem = io.imread('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Sunset_in_Manaus.jpg/640px-Sunset_in_Manaus.jpg')
cv2.imshow('Imagem Marvel', imagem)
cv2.waitKey(1000)