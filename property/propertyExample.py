#A setter can only be attached to a method that has first been converted into a property

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname_Set(self, name):
        first, second = name.split(" ")
        self.first = first
        self.last = second

    @fullname.deleter
    def fullname(self):
        del self.first
        del self.last
        print("Deleted")


emp_1 = Employee('John', 'Smith')

emp_1.first = "jim"
emp_1.fullname_Set = "sanjay sam"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# del emp_1.fullname