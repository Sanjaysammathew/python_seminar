#A static method is a method defined inside a class that does not depend 
# on the object (self) or the class (cls). 
# It is mainly used for utility or helper operations related to the class.

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} - {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


employee1 = Employee("Arun", "Manager")
employee2 = Employee("Rahul", "Cashier")
employee3 = Employee("Karthik", "Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

print(Employee.is_valid_position("Manager"))
print(Employee.is_valid_position("Developer"))