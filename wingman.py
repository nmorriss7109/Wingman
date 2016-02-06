from PIL import Image
import numpy as np
import urllib
import pynder
import os
import cv2


FBTOKEN = 'CAAGm0PX4ZCpsBAB4D6um6yJxiNKVB9llVCz3Gk82qayOtVf5LDCUVZAZCZA4xuqG2ArfCdI0HDDezFdqIteYAvpAWqQRQiyZAGRnAk4Cg5psZAVLCpdtHvExaBYljqR38bBQQI28uxIpmYHzMgsa0kctH9UDZBWCGtoWZCsY8mNZApVBBb4a9X2lJazkoL4vEvlAuBRE8ImFAqQZDZD'
FBID = '464891386855067'


session = pynder.Session(FBID, FBTOKEN)

def get_photos(users):
	for user in users:
		print user.name
		img = user.get_photos(width='640')
		for i in range(0, len(img)):
			filename = os.path.join('faces', user.name + str(i) + '.jpg')
			urllib.urlretrieve(img[i], filename)
			convert_to_bw(filename)


def convert_to_bw(filename):
	col = Image.open(filename)
	gray = col.convert('L')
	gray.save('faces_bw/' + filename[5:])
	face_cascade = cv2.CascadeClassifier('~/Downloads/Install-OpenCV-master/Ubuntu/OpenCV/opencv-3.1.0/data/haarcascades_cuda/haarcascade_frontalface_default.xml')
	print face_cascade.detectMultiScale(cv2.cvtColor(cv2.imread('faces_bw/' + filename[5:]), cv2.COLOR_BGR2GRAY), 1.3, 5)
	

get_photos(session.nearby_users())
