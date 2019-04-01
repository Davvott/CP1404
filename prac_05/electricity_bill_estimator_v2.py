# print('Welcome to the Electricity bill estimator')
#
# cents_per_kwh = int(input("Enter cents per kWh: "))
# daily_use = float(input("Enter daily use in kWh: "))
# billing_days = int(input("Enter number of billing days: "))
# total_bill = (cents_per_kwh/100 * daily_use) * billing_days
#
# print("Estimated bill: ${}".format(total_bill))


# Version II

TARIFFS = {11: 0.244618, 31: 0.136928}

print('Welcome to the Electricity bill estimator 2.0')
for key in TARIFFS:
    print("Tarriff {} is {} cents per hour".format(key, TARIFFS[key]))

correct_input = False


while not correct_input:

    try:
        tariff = int(input("Which tariff: "))
    except ValueError:
        print("Please enter an integer")
        continue

    if tariff not in TARIFFS:
        print("Tariff not found, try again")
    else:
        correct_input = True

daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
total_bill = (TARIFFS[tariff] * daily_use) * billing_days

print("Estimated bill: ${:,.2f}".format(total_bill))
