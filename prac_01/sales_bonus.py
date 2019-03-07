"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
#
# PROMPT = """(Q)UIT or Enter sales: $"""
#
# user_input = input(PROMPT).upper()
#
# while user_input != 'Q':
#
#     try:
#         user_input = float(user_input)
#         if user_input <= 0:
#             print("You have to earn more than that to qualify for a bonus!")
#
#         elif user_input >= 1000:
#             bonus = 0.15 * user_input
#             print('Your bonus is ${:.2f}, your total this month is ${:.2f}'.format(
#                 bonus, user_input+bonus))
#         else:
#             bonus = 0.1 * user_input
#             print('Your bonus is ${:.2f}, your total this month is ${:.2f}'.format(
#                 bonus, user_input+bonus))
#     except:u
#         print("Please enter a valid number or (Q)uit")
#
#     user_input = input(PROMPT).upper()
#

user_input = float(input("Enter sales: $"))
bonus = 0
if user_input <= 0:
    print('Your bonus is ${:.2f}, your total this month is ${:.2f}'.format(
        bonus, user_input+bonus))
elif user_input >= 1000:
    bonus = 0.15 * user_input
    print('Your bonus is ${:.2f}, your total this month is ${:.2f}'.format(
        bonus, user_input+bonus))
else:
    bonus = 0.1 * user_input
    print('Your bonus is ${:.2f}, your total this month is ${:.2f}'.format(
        bonus, user_input+bonus))
