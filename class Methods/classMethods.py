
# A class method is a method that works with the class itself, rather than a particular object.

# It uses the @classmethod decorator and takes cls as its first parameter.

class Student:

    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"


student1 = Student("Sanjay", 3.2)
student2 = Student("Sam", 2.0)


print(student1.get_info())
print(student2.get_info())

print(Student.get_count())