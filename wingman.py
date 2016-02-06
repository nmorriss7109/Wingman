import urllib
import pynder
import os.path


FBTOKEN = 'CAAGm0PX4ZCpsBAC1wdZASOlfEBKgKmkPHQk4ydsyc2rC9t70vQJ3Ia7rzS6Tkl60vNjt3cwj6NxBYXxXAMTF2ZAj9xEtFuJb1n9QDqMLSx4FTdXbrZAPni8Kl9gyOLwupwAWkZCF4LfWyfKvDHT5eJMy5iAYMXk8fNrwH04CXRYd6znDn4LMcTnqokzu3mEG6eM6ZBFAQMeQZDZD'
FBID = '464891386855067'

session = pynder.Session(FBID, FBTOKEN)

def get_photos(users):
	for user in users:
		print user.name
		img = user.get_photos(width='640')
		for i in range(0, len(img)):
			urllib.urlretrieve(img[i], os.path.join('faces', user.name + str(i) + '.jpg'))

get_photos(session.nearby_users())