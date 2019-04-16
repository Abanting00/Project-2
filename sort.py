import os, unittest

def child(file):

	# Check if file is available
	# while True:
	# 	# check if file is lock

	# 	# Exception handling maybe?
	# 	try:
	# 		fd = open()
	print(file)

def parent():
	files = ['new1.dat.txt', 'new2.dat.txt', 'new3.dat.txt']
	
	for i in range(3):
		child = os.fork()

		if child == 0:
			child(files[i])
			return

	os.wait()
	return

if __name__ == '__main__':
	parent()


