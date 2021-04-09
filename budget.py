class Budget:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount


    def deposit(self):
        amount = int(input(f"How much would you love to budget for {self.category}: \n"))
        self.amount += amount
        return f"Budget for {self.category} = {self.amount}" 

    def withdraw(self):
        withdraw = int(input(f"How much do you want to withdraw from {self.category}: \n"))
        self.amount -= withdraw

    def check_balance(self):
        return f"Remaining balance for {self.category} = {self.amount}"

    def transfer(self):
        amount = int(input(f"How much would you love to transfer to {self.category}: \n"))
        self.amount += amount
        return f"Current budget for {self.category} = {self.amount}"
        



food = Budget("Food", 0)
print(food.deposit())
print("===== * ===== * =====")
print(food.withdraw())
print("===== * ===== * =====")
print(food.check_balance())
print("===== * ===== * =====")
print(food.transfer())
print("===== * ===== * =====")
