#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: December 2019
# This program reverses a list
# with user input


def reverse_lst(new_lst):
    # this function reverses a list

    new_lst.reverse()


def main():
    # this function creates a list

    lst_num = []
    print("Let's reverse the numbers you enter")

    try:
        first = int(input("Enter the first number: "))
        second = int(input("Enter the second number: "))
        third = int(input("Enter the third number: "))
        fourth = int(input("Enter the fourth number: "))
        print("")

        lst_num.append(first)
        lst_num.append(second)
        lst_num.append(third)
        lst_num.append(fourth)

        reverse_lst(lst_num)

        for single_number in lst_num:
            print("{0}, ".format(single_number), end="")

    except Exception:
        print("You did not enter an integer")


if __name__ == "__main__":
    main()
