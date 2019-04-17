import os, unittest, fcntl

def child(file):

	#  Check if file is lock or unlock
	while True:
		# Exception handling maybe?
		try:
			fd = open('datafile.dat.txt','r+')
			fcntl.flock(fd, fcntl.LOCK_EX  | fcntl.LOCK_NB)
			break
		except IOError:
			continue

	# file is open for writing, lock the file
	fcntl.flock(fd, fcntl.LOCK_EX)
	fd2 = open(file,'r')

	main = []
	for num in fd:
		main.append(int(num.rstrip('\n')))

	new = []
	for num in fd2:
		new.append(int(num.rstrip('\n')))
	new.sort()

	# Merge the two sorted list
	main = merge(main,new)

	# put the file descriptor to the beginning
	fd.seek(0,0)

	# write to the file
	for num in main:
		fd.write("%d\n" % num)

	# Close the open files
	fd2.close()

	# unlock the main file
	fcntl.flock(fd, fcntl.LOCK_UN)
	

# Merge two sorted list into one list
def merge(l1,l2):
	res = []
	i = j = k = 0
	
	while i < len(l1) and j < len(l2):
		if l1[i] < l2[j]:
			res.append(l1[i])
			i += 1
		else:
			res.append(l2[j])
			j += 1

	res = res + l1[i:]
	res = res + l2[j:]

	return res


def parent():
	files = ['new1.dat.txt', 'new2.dat.txt', 'new3.dat.txt']
	c = os.fork()
	count = 0

	while c != 0 and count < 2:
		count += 1
		c = os.fork()

	if c == 0:
		child(files[count])
	else:
		for i in range(3):
			fin = os.waitpid(0,0)

		print("Finish Sorting...")
		print("Initializing Test")
		os.system("python3 sort_test.py")
	return

if __name__ == '__main__':
	parent()

