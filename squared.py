#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program squares each number from 0 up to the users number


def main():
    # This function squares each number from 0 up to the users number
    counter = 0
    answer = 0

    # Input
    integer_s = input("Enter an integer >= 0: ")
    print("")

    # Process and Output
    try:
        integer = int(integer_s)
        if integer < 0:
            print("You did not enter a positive integer.")
        for counter in range(integer + 1):
            answer = counter ** 2
            print("{0}² = {1}² ".format(counter, answer))

    except Exception:
        print("Invalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
