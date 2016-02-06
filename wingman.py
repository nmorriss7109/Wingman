import pynder

FBTOKEN = 'CAAGm0PX4ZCpsBAB55ZAL2tuyB9vuWjPKIdEjw7xGLGZAE1M6IgFD1ZB7ZBcgZB0pxnXnTEEWnTndkNVW7uWremhUlneSa3elJ9GrsOejYFA7yR0OfPNiMb3QiIOcpo4WTBGex27Q0KJoXTYZBlrLNzRuhqqGaDA7R6FQ6v4AKe0bHpK7Vq8Na8zaiq5QpOQ4VIZCwM8HhWifbwZDZD'
FBID = '464891386855067'

session = pynder.Session(FBID, FBTOKEN)
users = session.nearby_users()

for user in users[:1]:
	print user.name
	print user.get_photos(width='640')
