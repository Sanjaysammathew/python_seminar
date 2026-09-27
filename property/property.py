# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#
#          Benefit: Add additional logic when read, write, or delete attributes
#
#          Gives you getter, setter, and deleter method

#A setter can only be attached to a method that has first been converted into a property

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')

emp_1.first="Jim"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())


