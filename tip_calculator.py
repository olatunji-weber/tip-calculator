# 1.  Ask user to enter charge for food.
charge = input("What is the Cost of the Food? ")

# 1.  Calculate 18 percent tip
tip = (charge * (18 / 100))

# 2.  Calculate 7 percent sales tax food charge
tax = (charge * (7 / 100))

# 3.  Display each of amount.
print(f"The Charge for the Food is: {charge}")
print(f"The Tip is: {tip}")
print(f"The Tax is: {tax}")

# 4.  Add everything together and display the charge of the food, plus tip and sales tax.
customer_pay = charge + tip + tax
print(f"The Customer Pays: {customer_pay}")