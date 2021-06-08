#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on June 8, 2021
# Generates 5 random numbers from 1 and 100

import random


def largest_number(list_of_numbers):
    maximum = list_of_numbers[0]
    for number in list_of_numbers:
        if number > maximum:
            maximum = number
    return maximum


def main():
    random_numbers = []
    loop_counter = 0
    for loop_counter in range(10):
        loop_counter = loop_counter + 1
        number = random.randint(1, 100)
        random_numbers.append(number)
    largest_number(random_numbers)
    largest_num = largest_number(random_numbers)
    print("Your random numbers are: {}".format(random_numbers))
    print("The largest number is: {}".format(largest_num))
    print("Done.")


if __name__ == "__main__":
    main()
