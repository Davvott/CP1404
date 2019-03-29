# print('Welcome to the Electricity bill estimator')
#
# cents_per_kwh = int(input("Enter cents per kWh: "))
# daily_use = float(input("Enter daily use in kWh: "))
# billing_days = int(input("Enter number of billing days: "))
# total_bill = (cents_per_kwh/100 * daily_use) * billing_days
#
# print("Estimated bill: ${}".format(total_bill))


# Version II

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print('Welcome to the Electricity bill estimator 2.0')

tariff = int(input("Which tariff? 11 or 31: "))
if tariff == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_31

daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
total_bill = (tariff * daily_use) * billing_days

print("Estimated bill: ${:.2f}".format(total_bill))
