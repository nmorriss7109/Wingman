from PIL import Image
import numpy as np
import urllib
import pynder
import os
import cv2

FBTOKEN = 'CAAGm0PX4ZCpsBAFzSZARBkZAPQSRGnLnQltUsLduuRKqcZBYBQPPe7F6u78ZAtsdmBdJSyMTtCImXE8iZBhqCkb1o2IkkENaVJKckQUZAOHkyEw82eurzZCDOcmBSZAIBMoAr1Kn5jp4UoANcyqiGmL3ai1T5JNv2xMeZA3eicXPsH8ksY8oeypw2FjeRlnSgNnDxNoVRaKlOfnwZDZD'
FBID = '464891386855067'


session = pynder.Session(FBID, FBTOKEN)

def get_photos(users):
	for user in users:
		print user.name
		img = user.get_photos(width='640')
		for i in range(0, len(img)):
			filename = os.path.join('faces', user.name + str(i) + '.jpg')
			urllib.urlretrieve(img[i], filename)
			cv_convert(filename)


def cv_convert(filename):
	col = Image.open(filename)
	gray = col.convert('L')
	gray.save('faces_bw/' + filename[5:])
	cascade_fn = '/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml'
	face_cascade = cv2.CascadeClassifier(cascade_fn)
	faces = face_cascade.detectMultiScale(cv2.imread('faces_bw/' + filename[5:]), 1.3, 5)
	faces = np.array(faces)
	faces = faces.tolist()
	print faces
	if len(faces) == 1:
		lst = faces[0]
		gray = gray.crop((lst[0], lst[1], lst[0]+lst[2], lst[1]+lst[3]))
		gray.save('processed_images/' + filename[5:])

	else:
		print "no faces/too many faces"


	

get_photos(session.nearby_users())
