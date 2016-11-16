#Lazu13 (Tomasz Laz)

import unittest
from kol2_gr2 import *


class test_ClassDiary(unittest.TestCase):
	def setUp(self):
		self.student = Student("Tomasz", "Laz")
		self.student2 = Student("Tomasz", "Test")
		self.students = []
		self.students.append(self.student)
		self.students.append(self.student)
		self.classDiary = ClassDiary(SchoolClass("A", self.students))

	def test_void_addAtendance_method_returns_None(self):
		self.assertEqual(None, self.classDiary.addAtendance(self.student))


class test_Student(unittest.TestCase):
	def test_init(self):
		self.assertRaises(Exception, Student, 1, 2 )


class test_SchoolClass(unittest.TestCase):
	def setUp(self):
		self.student = Student("Tomasz", "Laz")
		self.student2 = Student("Tomasz", "Test")
		self.students = []
		self.students.append(self.student)
		self.students.append(self.student)

	def test_init(self):
		self.assertRaises(Exception, SchoolClass, 1, self.students)


if __name__ == "__main__":
	unittest.main()