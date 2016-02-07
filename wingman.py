from PIL import Image
import numpy as np
import urllib
import pynder
import os
import cv2

FBTOKEN = 'CAAGm0PX4ZCpsBAADgmzHMA5UTVVuZA7SE39VNZAXVPvZCzXRQVElAiZCNMw36XWEDZAWnI3ZAWiowVLNZApW8DgPZA3PCxH0MCWzMrFc2hxY5ceE6mE1yAITxeSNRe1BkJ9Jxh04zyLLKHRONIJPMkrywQ3mmtSnzoOwB53bHksD7ZALp9z9s7Q7Wy7Yrgtg374ZB2dWwUgZBPwEFgZDZD'
FBID = '464891386855067'


session = pynder.Session(FBID, FBTOKEN)

def get_photos(users):
	for user in users:
		print user.name
		sex = user.gender
		img = user.get_photos(width='640')
		for i in range(0, len(img)):
			filename = os.path.join('faces', user.name + '_' + sex + str(i) + '.jpg')
			urllib.urlretrieve(img[i], filename)
			cv_convert(filename)


def cv_convert(filename):
	col = Image.open(filename)
	gray = col.convert('L')
	gray.save(filename)
	cascade_fn = '/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml'
	face_cascade = cv2.CascadeClassifier(cascade_fn)
	faces = face_cascade.detectMultiScale(cv2.imread(filename), 1.3, 5)
	faces = np.array(faces)
	faces = faces.tolist()
	print faces
	if len(faces) == 1:
		lst = faces[0]
		gray = gray.crop((lst[0], lst[1], lst[0]+lst[2], lst[1]+lst[3]))
		gray.save(filename)

	else:
		os.remove(filename)
		print "no faces/too many faces"


	

get_photos(session.nearby_users())
