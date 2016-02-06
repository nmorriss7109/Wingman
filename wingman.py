from PIL import Image
import numpy as np
import urllib
import pynder
import os
import cv2

FBTOKEN = 'CAAGm0PX4ZCpsBACgdud69wZCOl5G2Lj5u8SP1C9xJi3Grt5UmUYO5uFYkS5a162dfwmABs1ZABYeO2yqTZBUmhnwJ0J7WYfC0OMgR5103N9cKCrgLjtF3sm6kAoEZAfmQGX2ztlNtLKdOLuf9rKqWkj4HEih6q5JurQIrRlNBjF8AZC3buLvPDckNl5cia9pEle9FKDD37DwZDZD'
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

	for n in face:
		if n == face[0]:
			print n
			pt1 = [n[0], n[1]]
			pt2 = [n[0] + n[2], n[1] + n[3]]
			print pt1
			print "hello"
			print pt2
			cv2.rectangle(cv2.imread('faces_bw/' + filename[5:]), (pt1[0], pt1[1]) , (pt2[0], pt2[1]), (255, 0, 0), 5, 8, 0))
			cv2.waitKey(0)
			cv2.destroyAllWindows()

		else:
			print "too many faces"

	

get_photos(session.nearby_users())
