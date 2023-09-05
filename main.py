# Write your code here
# print("Prices:\nBubblegum: $2\nToffee: $0.2\nIce cream: $5\nMilk chocolate: $4\nDoughnut: $2.5\nPancake: $3.2")
bubbleGum = 202
toffee = 118
iceCream = 2250
milkChocolate = 1680
doughnut = 1075
pancake = 80
income = bubbleGum + toffee + iceCream + milkChocolate + doughnut + pancake + 0.0

print("Earned amount:")
print("Bubblegum: $" + str(bubbleGum))
print("Toffee: $" + str(toffee))
print("Ice Cream: $" + str(iceCream))
print("Milk Chocolate: $" + str(milkChocolate))
print("Doughnut: $" + str(doughnut))
print("Pancake: $" + str(pancake))

print()

print("Income: $" + str(income))

print("Staff expenses:")
staff_expenses = int(input())

print("Other expenses:")
other_expenses = int(input())

net_income = income - (staff_expenses + other_expenses)

print("Net income: $", end=str(net_income))
