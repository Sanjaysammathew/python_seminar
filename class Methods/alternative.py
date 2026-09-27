class BankAccount:

    bank_name = "ABC Bank"

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    @classmethod
    def from_string(cls, data):
        name, number, balance = data.split(",")
        return cls(name, number, float(balance))


# Normal object creation
account1 = BankAccount("Sanjay", "ACC101", 50000)

# Creating object using class method
account2 = BankAccount.from_string("Rahul,ACC102,35000")

print(account1.account_holder)
print(account2.account_holder)
print(account2.balance)