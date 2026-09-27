# Class method: Uses @classmethod and cls to access or modify class-level data.

# Static method: Uses @staticmethod and does not need self or cls, mainly for utility operations.

#class method access class data automatically and static method cannot able to acess automatically

class Employee:
    company = "ABC Technologies"

    @classmethod
    def show_company(cls):
        print(cls.company)


Employee.show_company()


class Employee:
    company = "ABC Technologies"

    @staticmethod
    def show_company():
        print(Employee.company)


Employee.show_company()