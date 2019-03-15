"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result = calc_result(score)
    print(result)


def calc_result(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()