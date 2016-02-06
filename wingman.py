from PIL import Image
import numpy as np
import urllib
import pynder
import os
import cv2

FBTOKEN = 'CAAGm0PX4ZCpsBAL77EmVZAV8gxHAal1p3HDB17RnBF6qkjEBM2dk1dnlgFOX1HjLZA2TB0vq0cjoJL4ZAG852ZBOzUb6lsunKXhrdnHusJnPb36VkWbojdCfz1mxy0K6fx84rmuCqh2t8jZC6j5ZAcUzWViUdhNptEP8JvuMcLLy3lOZCpbmqCMZCp25I6r18pNUG6v5Kned2cQZDZD'
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
	cascade_fn = '/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml'
	face_cascade = cv2.CascadeClassifier(cascade_fn)
	face = face_cascade.detectMultiScale(cv2.imread('faces_bw/' + filename[5:]), 1.3, 5)
	face = np.array(face)
	face = face.tolist()
	print face
	print len(face)
	if len(face) == 1:
		lst = face[0]
		pt1 = [lst[0], lst[1]]
		pt2 = [lst[0] + lst[2], lst[1] + lst[3]]
		print pt1
		print "hello"
		print pt2
		cv2.rectangle(cv2.imread('faces_bw/' + filename[5:]), (pt1[0], pt1[1]) , (pt2[0], pt2[1]), (255, 0, 0), 5, 8, 0)

	else:
		print "no faces/too many faces"

	

get_photos(session.nearby_users())
