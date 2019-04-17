import unittest
from sort import parent

class TestSort(unittest.TestCase):
	def testFileOutput(self):
		# Open answer file and modified file
		fd = open('ans.dat.txt','r')
		fd2 = open('datafile.dat.txt','r')

		main = []
		answer = []
		for num in fd:
			main.append(int(num.rstrip('\n')))

		for num in fd2:
			answer.append(int(num.rstrip('\n')))

		fd.close()
		fd2.close()

		self.assertEqual(main,answer)


if __name__ == '__main__':
	unittest.main()
	unittest.main()