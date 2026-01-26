class Course:
    def __init__(self, name, groups = None):
        self.__name = name
        self.__groups = groups or []
    
    def add_group(self, group):
        self.__groups.append(group)

    def get_name(self):
        return self.__name
    
    def get_groups(self):
        return self.__groups
    
    def get_all_students(self):
        student_list = []
        for group in self.__groups:
                student_list.extend(group.get_students())
        return student_list
    
    def find_student(self, name_or_surname):
        student_list = []
        for group in self.__groups:
                student_list.extend(group.get_students())
        for student in student_list:
            if student.name == name_or_surname or student.surname == name_or_surname:
                return student

    
    def __repr__(self):
        return f'Course: {self.__name} \ngroups: {self.__groups}'


class Group:
    def __init__(self, name, students = None):
        self.name = name
        self.students = students or []
    
    def add_students(self, students):
        for student in students:
            self.students.append(student)
        return students
    
    def get_students(self):
        return self.students

class Student:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
    def __repr__(self):
        return f'Student: {self.name}, {self.surname}'

student_1 = Student("Bob", "Brown")
student_2 = Student("Carl", "Jonson")
student_3 = Student("Peter", "Parker")

group1 = Group("#1")
group1.add_students([student_1, student_2])

group2 = Group("#2")
group2.add_students([student_3])

course = Course("Python")
course.add_group(group1)
course.add_group(group2)

assert course.get_name() == "Python"
assert len(course.get_groups()) == 2

print (course.get_all_students())
assert course.get_all_students() == [student_1, student_2, student_3]

assert course.find_student("Bob") == student_1
assert course.find_student("Parker") == student_3
assert course.find_student("Noname") is None

print("✅ All tests passed")