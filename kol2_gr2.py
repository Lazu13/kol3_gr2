#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
#
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class Student(object):
	def __init__(self, *args):
		for i in args:
			if isinstance(i,str) == False:
				raise Exception
		self.name = args[0]
		self.surname = args[1]

class SchoolClass(object):
	def __init__(self, className, students):
		if isinstance(className,str) == False:
			raise Exception
		for i in students:
			if isinstance(i, Student) == False:
				raise Exception
		
		self.className = className
		self.students = students
		self.students = list(set(self.students))



class ClassDiary(object):
	def __init__(self, schoolClass):
		self.schoolClass = schoolClass
		self.diary = {i: [] for i in self.schoolClass.students}
		self.attendance = {i: 0 for i in self.schoolClass.students}

	def addAtendance(self,student):
		for i in self.schoolClass.students:
			if i.name == student.name and i.surname == student.surname:
				self.attendance[i] += 1

	def addGrade(self, student, grade):
		if isinstance(grade, int) == False:
			raise Exception
		if isinstance(student, Student) == False:
			raise Exception
		for i in self.schoolClass.students:
			if i.name == student.name and i.surname == student.surname:
				self.diary[i].append(grade)

	def getAttendance(self,student):
		if isinstance(student, Student) == False:
			raise Exception
		for i in self.schoolClass.students:
			if i.name == student.name and i.surname == student.surname:
				return self.attendance[i]


def main():
	student1 = Student("Tomasz","Laz")
	student2 = Student("Adam","Nowak")

	students = []
	students.append(student1)
	students.append(student1)
	schoolClass = SchoolClass("1A", students)
	
	class1 = ClassDiary(schoolClass)
	class1.addAtendance(student1)
	class1.addGrade(student1, 5)

	print class1.getAttendance(student1)


if __name__ == "__main__":
	main()
