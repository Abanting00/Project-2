import os, unittest, fcntl, time

def child(file):

	#  Check if file is lock or unlock
	fd = open('datafile.dat.txt','r+')
	while True:
		# Exception handling to check if we can obtain a lock
		try:
			fcntl.flock(fd, fcntl.LOCK_EX  | fcntl.LOCK_NB)
			break
		except IOError:
			time.sleep(.03)

	# file is open for writing
	fd2 = open(file,'r')

	# Create a list of numbers from files
	main = []
	for num in fd:
		if num != '':
			main.append(int(num.rstrip()))

	new = []
	for num in fd2:
		if num != '':
			new.append(int(num.rstrip()))
	new.sort()

	# Merge the two sorted list
	main = merge(main,new)
	# put the file descriptor to the beginning
	fd.seek(0,0)

	# write to the file
	print("PID: %d File: %s is writing..." % (os.getpid(), file))
	for num in main:
		fd.write("%d\n" % num)
	print("Finished writing\n")

	# unlock the main file
	fcntl.flock(fd, fcntl.LOCK_UN)

	# Close the open files
	fd2.close()
	fd.close()
	os._exit(0);

# Merge two sorted list into one list (MergeSort Algorithm)
def merge(l1,l2):
	res = [0] * (len(l1) + len(l2))
	i = j = k = 0
	
	while i < len(l1) and j < len(l2):
		if l1[i] < l2[j]:
			res[k] = l1[i]
			i += 1
		else:
			res[k] = l2[j]
			j += 1
		k += 1

	while i < len(l1):
		res[k] = l1[i]
		i += 1
		k += 1

	while j < len(l2):
		res[k] = l2[j]
		j += 1
		k += 1

	return res

# Parent create 3 process that writes to the main file
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
	os.system("cp original.dat.txt datafile.dat.txt")
	parent()

