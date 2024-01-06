"""Class inheritance"""
class Person:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Student(Person):
    def get_student_first_name(self):
        return self.first_name
    
    def get_student_full_name(self):
        return f"{self.first_name} {self.last_name}"
    

student = Student("Temur", "Yusupov", 16)
print(student.get_student_full_name())