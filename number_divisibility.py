#!/usr/bin/env python3
# Created by: Elohim Conteh
# Created on: November 14, 2026
# This program checks if a positive integer is divisible by 2, 5, 7, or any combination.


def main() -> None:
    # Initial greeting
    print(
        "Welcome! This program checks if a positive integer is divisible by 2, 5, 7, or any combination."
    )
    print()

    # Input
    user_input_string = input("Enter a positive integer: ")

    # Process & Output
    try:
        user_number = int(user_input_string)

        # Extra Functionality #1: Check if positive
        if user_number <= 0:
            print(
                "Error: "
                + str(user_number)
                + " is not a positive integer. Please enter a number greater than 0."
            )
        else:
            divisors = ""
            non_divisors = ""

            # Check 2
            if user_number % 2 == 0:
                divisors = divisors + "2 "
            else:
                non_divisors = non_divisors + "2 "

            # Check 5
            if user_number % 5 == 0:
                divisors = divisors + "5 "
            else:
                non_divisors = non_divisors + "5 "

            # Check 7
            if user_number % 7 == 0:
                divisors = divisors + "7 "
            else:
                non_divisors = non_divisors + "7 "

            # Display results
            if divisors != "":
                print(str(user_number) + " is divisible by: " + divisors)
            else:
                print(str(user_number) + " is not divisible by 2, 5, or 7.")

            # Extra Functionality #2: Show non-divisors
            if non_divisors != "":
                print(
                    "Note: "
                    + str(user_number)
                    + " is NOT divisible by: "
                    + non_divisors
                )

    except ValueError:
        print(
            "Error: '"
            + user_input_string
            + "' is not a valid integer. Please enter a positive integer."
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
