#Lazu13 (Tomasz Laz)
import sys
import unittest
sys.path.append("../")
from kol2_gr2 import *


'''
test class ClassDiary
'''
class test_ClassDiary(unittest.TestCase):
	def setUp(self):
		self.student = Student("Tomasz", "Laz")
		self.student2 = Student("Tomasz", "Test")
		self.students = []
		self.students.append(self.student)
		self.students.append(self.student2)
		self.school_class = SchoolClass("A", self.students)
		self.class_diary = ClassDiary(self.school_class)

	def test_init_contains_school_class(self):
		self.assertEqual(self.class_diary.schoolClass, self.school_class)

	def test_init_contains_lists_with_proper_length(self):
		self.assertEqual(len(self.students), len(self.class_diary.attendance))
		self.assertEqual(len(self.students), len(self.class_diary.diary))

	def test_void_addAtendance_method_returns_None(self):
		self.assertEqual(None, self.class_diary.addAtendance(self.student))

	def test_void_addAttendance_method_changes_attendance(self):
		self.class_diary.addAtendance(self.student)
		self.assertEqual(1, self.class_diary.attendance[self.student])

	def test_int_getAttendance_method_returns_student_attendance(self):
		self.class_diary.addAtendance(self.student2)
		self.assertEqual(1, self.class_diary.getAttendance(self.student2))

	def test_int_getAttendance_method_returns_0(self):
		self.assertEqual(0, self.class_diary.getAttendance(self.student))

	def test_int_getAttendance_method_raise_exception(self):
		self.assertRaises(Exception, self.class_diary.getAttendance, "Student")

	def test_void_addGrade_raise_student_type_exception(self):
		self.assertRaises(Exception, self.class_diary.addGrade, "Student", 1)

	def test_void_addGrade_raise_grade_type_exception(self):
		self.assertRaises(Exception, self.class_diary.addGrade, self.student, "1")

	def test_void_addGrade_changes_grade_for_student(self):
		grade = 5
		self.class_diary.addGrade(self.student, grade)
		self.assertIn(grade, self.class_diary.diary[self.student])

	def test_void_addGrade_does_not_change_grade_for_student(self):
		self.assertEqual([], self.class_diary.diary[self.student])


'''
test class Student
'''
class test_Student(unittest.TestCase):
	def setUp(self):
		self.name = "Tomasz"
		self.surname = "Laz"
		self.student = Student(self.name, self.surname)

	def test_init_raise_exception(self):
		self.assertRaises(Exception, Student, 1, 2)

	def test_init_contains_student_name(self):
		self.assertEqual(self.student.name, self.name)

	def test_init_contains_student_suname(self):
		self.assertEqual(self.student.surname, self.surname)


'''
test class SchoolClass
'''
class test_SchoolClass(unittest.TestCase):
	def setUp(self):
		self.student = Student("Tomasz", "Laz")
		self.student2 = Student("Tomasz", "Test")
		self.students = []
		self.students.append(self.student)
		self.students.append(self.student2)
		self.class_name = "1D"
		self.school_class = SchoolClass(self.class_name, self.students)

	def test_init_raise_exception(self):
		self.assertRaises(Exception, SchoolClass, 1, self.students)

	def test_init_contains_className(self):
		self.assertEqual(self.school_class.className, self.class_name)

	def test_init_contains_list_with_student(self):
		self.assertIn(self.student, self.school_class.students)

	def test_init_contains_list_with_only_one_student(self):
		self.students.append(self.student)
		self.school_class = SchoolClass(self.class_name, self.students)
		count_student = self.school_class.students.count(self.student)
		self.assertEqual(1, count_student)


if __name__ == "__main__":
	unittest.main()