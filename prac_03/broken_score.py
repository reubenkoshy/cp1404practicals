"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))


def check_score(value):
    if value < 0 or value > 100:
        message = "Invalid score"
    elif value < 50:
        message = "Bad"
    elif 90 > value:
        message = "Passable"
    else:
        message = "Excellent"
    return message


print(check_score(score))
