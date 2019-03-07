
# Shopr equires a small program too allow them to quickly wok out the total price for a
# number of items and the price of each item

print("Welcome to the Shop Calculator")
num_items = int(input("Please enter the number of items to calculate: "))

# Check num_items
while type(num_items) != int or num_items < 0:
    print("Please enter a positive integer!")
    try:
        num_items = int(input("Please enter the number of items to calculate: "))
    except ValueError:
        print("That is not a valid entry.")

count = 1
total_price = 0

while count <= num_items:

    while True:
        try:
            user_input = float(input("Price of item: ".format(count)))
            count += 1
            break
        except ValueError:
            print("That is not a valid price. Try again.")

    total_price += user_input

if total_price > 100:
    total_price -= (0.1 * total_price)
print("Total price for {} items is ${:.2f}".format(num_items, total_price))





