#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program squares each number from 0 up to the user input


def main():
    # This program squares each number from 0 up to the user input
    counter = 0
    squared_answer = 0

    # Input
    integer_as_string = input("Enter an integer >= 0: ")
    print("")

    # Process and Output
    try:
        integer_as_int = int(integer_as_string)
        if integer_as_int < 0:
            print("Please enter a positive number.")
        for counter in range(integer_as_int + 1):
            squared_answer = counter**2
            print("{0}² = {1}² ".format(counter, squared_answer))

    except Exception:
        print("Please input a valid number.")

    print("\nDone.")


if __name__ == "__main__":
    main()
