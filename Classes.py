class Grade():
    def __init__(self, name, teachers, students):
        self._name = name
        self._teachers = teachers
        self._students = students
    def show_students(self):
        print(self._students)
    def show_teachers(self):
        print(self._teachers)
class Teacher:
    def __init__(self, grades, subject):
        self._grades = grades
        self._subject = subject
class Student:
    def __init__(self, _grade, name, subjects, parents):
        self._grade_ = _grade
        self._name = name
        self._subjects = subjects
        self._parents = parents
    def show_parents(self):
        print(self._parents)
    def show_subj(self):
        print(self._subjects)
class School:
    def __init__(self, grades_number, grades_names):
        self._grades_number = grades_number
        self._grades_names = grades_names
    def get_classes(self):
        print(self._grades_names)