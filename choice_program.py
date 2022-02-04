#!/usr/bin/env python3
# Created by: Ketia Gaelle Kaze
# Created on: Jan. 29, 2022
# This program asks the user to enter one
# of the numbers given to choose from and then
# it displays the program that corresponds
# to that number they entered.


def generate_even_numbers(list_string):
    # this function determines even numbers in a list
    # create an empty list
    list_of_int = []
    # uses a for loop find the even numbers in a list
    for integer in list_string:

        # convert string to int
        try:

            a_num = int(integer)
            if a_num % 2 == 0:
                # appends the number that is even to the empty list
                list_of_int.append(a_num)
                list_of_int = sorted(list_of_int)
        except Exception:
            print("Invalid Input")
    return list_of_int


def common_element(first_list, second_list):
    # this function determines common elements in two lists
    # create an empty list
    result = []
    # uses a for loop to find the elements that are common in both lists
    for element in first_list:
        if element in second_list:
            # appends the elements that are common to the list.
            result.append(element)
    return result


def first_occur_and_last_occur(arr, num, target_num):
    # this function determines and first and last time
    # a number occurs in a list.
    first_occur = -1
    last_occur = -1
    # uses a loop to determine numbers in the list
    for counter in range(0, num):
        if (target_num != arr[counter]):
            continue
        if (first_occur == -1):
            first_occur = counter
        last_occur = counter
    # uses an if statement to display the first and last occurence of a number
    if (first_occur != -1):
        print("First Occurrence of {}= ".format(target_num), first_occur,
              " \nLast Occurrence of {} = ".format(target_num), last_occur)
    else:
        print("{} is not found in the list".format(target_num))


def main():
    # Display the opening message to the user
    print("Welcome to the house of coding!")
    # Ask the user the program they want to run
    print("Which of these programs would you like to run ?")
    print()
    # Display the choice of programs
    print("1:generate even numbers. ")
    print("2:common elements in a list.")
    print("3:first and last occurence of a number in a list.")
    print()

    # get user input
    user_input = input("Enter 1,2 or 3: ")
    # convert from string to int
    try:
        user_input = int(user_input)
        if user_input == 1:
            # Display the first program to the user
            # get user input
            user_input = input("Enter a list of integers: ")
            # create an empty list
            list_of_string = []
            # populate the empty list by splitting the user inputs
            # to create a list
            list_of_string = user_input.split(",")
            # generate even numbers
            final_list_user = generate_even_numbers(list_of_string)
            # Display the generated even numbers
            print("The even numbers are: {}".format(final_list_user))
            print()

        elif user_input == 2:
            # Display the second program to the user
            # get user input
            list1 = input("Enter the first list: ")
            list2 = input("Enter the second list: ")
            # create an empty list
            list_of_elements = []
            # populate the first empty list with the first user's input
            # and split them to create a list
            list_of_elements = list1.split(",")
            # create another empty list
            list_of_elements_1 = []
            # populate the second empty list with the second user's input
            # and split them to create a list
            list_of_elements_1 = list2.split(",")
            common_elements = common_element(list_of_elements,
                                             list_of_elements_1)
            # Display the common elements in a list
            print("The common elements is: {}".format(common_elements))
            print()

        elif user_input == 3:
            # Display the third program to the user
            # get user input
            str_of_num = input("Enter a list of integers: ")
            num = int(input("Enter the target number:  "))
            # create an empty list
            arr = []
            # populate the empty list with the first user's input
            # and split them to create a list
            arr_string = str_of_num.split(",")
            for str_num in arr_string:
                # converting string to int
                try:
                    a_num = int(str_num)
                    # append the converted numbers to the empty list
                    arr.append(a_num)
                    arr = sorted(arr)
                    # catch invalid inputs
                except Exception:
                    print("Some variables are not valid.")

            # Display the list of numbers
            print("In the list: {}".format(arr))
            number = len(arr)
            first_occur_and_last_occur(arr, number, num)
            # catch invalid inputs
        else:
            print("{} is not a valid input".format(user_input))
    except Exception:
        print("Invalid input")
        # Display the closing message
    print("Thank you for participating!")


if __name__ == "__main__":
    main()
