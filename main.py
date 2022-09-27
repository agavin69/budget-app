#MAIN FILE

import budget


food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(18.89, "Restaurants")

print(food.get_balance())

clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(26.55)

print(food)
print(clothing)