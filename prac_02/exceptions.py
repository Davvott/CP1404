try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        denominator = 1
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Value error occurs when user passes non-int input
# ZeroDivisionError occur swhen denominator == 0
# Avoid ZDE; if selection; or; try,except in while loop
