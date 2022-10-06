import time

while True:
	try:
		print("Sleeping for 5 secs")
		time.sleep(5)
	except BaseException:
		print("nope not gonna let you exit")
