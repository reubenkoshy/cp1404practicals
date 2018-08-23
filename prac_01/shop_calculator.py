"""
Expected output:
Number of items: 3
Price of item: 100
Price of item 35.56
Price of item: 3.24
Total price for 3 items is 124.92
"""

total = 0
numberItems = int(input("Number of items: "))
while numberItems < 0:
    print("Invalid number of items")
    numberItems = int(input("Number of items: "))
for i in range(numberItems):
    price = float(input("Price of item: $"))
    total += price


if total > 100:
    total *= 0.9
print("Total price for", numberItems, "items is", total)

