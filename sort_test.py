import unittest

class TestSort(unittest.TestCase):
	def testFileOutput(self):
		# Open answer file and modified file
		fd = open('ans.dat.txt','r')
		fd2 = open('datafile.dat.txt','r')

		main = []
		answer = []
		for num in fd:
			if num != '':
				main.append(int(num.rstrip()))

		for num in fd2:
			if num != '':
				answer.append(int(num.rstrip()))

		fd.close()
		fd2.close()

		# Check if both lists are equal
		self.assertEqual(answer,main)
		self.test_passed = True

	def setUp(self):
		self.test_passed = False

	# If test failed, append "Wrong" at end of wrong.txt
	def tearDown(self):
		if not self.test_passed:
			fd = open('wrong.txt','a+')
			fd.write("%s\n" % "Wrong")

			fd.close()

if __name__ == '__main__':
	unittest.main()