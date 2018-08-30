import random


def main():

    numbers_per_line = 6
    min_number = 1
    max_number = 45

    number_picks = int(input("How many quick picks? "))
    while number_picks < 0:
        print("Invalid Number of Quick Picks!")
        number_picks = int(input("How many quick picks? "))

    for i in range(number_picks):
        quick_pick = []
        for j in range(numbers_per_line):
            number = random.randint(min_number, max_number)
            while number in quick_pick:
                number = random.randint(min_number, max_number)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
