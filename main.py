# Import the colorama package to colorize console
from colorama import *

# Create an empty list
names = []

# Display the Menu
print("1.Create")
print("2.Read")
print("3.Update")
print("4.Delete")
print("0.Exit")
print("-----------------------------------")

# This condition will executed as long as the condition is True
while True:
    select = int(input(f"{Fore.WHITE}Select an option: "))
    print("-----------------------------------")

    # if select is equal to zero, exit the program by using
    # break function
    if select == 0:
        print("Exiting...")
        break

    # while select is not equal to zero, keep asking the user
    while select != 0:
        # Create
        # if select is equal to 1 ask the user to add their name
        if select == 1:
            user = input(f"{Fore.WHITE}Enter a name: ")
            print("-----------------------------------")

            # Adding the inputted name in user variable to the list names
            names.append(user)
            print(f"{user} added successfully.")
            print("-----------------------------------")

        # Read
        elif select == 2:
            print("Read | List of Names:")
            print("-----------------------------------")
            # Display the names from the List using for loop
            for i in names:
                print(i)
            print("-----------------------------------")
        # Update
        elif select == 3:
            print("Update | List of Names:")
            print("-----------------------------------")
            # Display the names from the List using for loop
            for i in names:
                print(i)
            print("-----------------------------------")
            update = input(f"{Fore.WHITE}Enter a name: ")
            change = input(f"{Fore.WHITE}Change to: ")
            print("-----------------------------------")

            # checking update variable
            # if update variable not in names List
            # Throws an error Name not in List
            if update not in names:
                print("Name not in List")

            # checking update variable
            # if update variable in names List
            # Remove the name that have been inputted in update variable then
            # Add a new name that have been inputted in change variable to the List
            if update in names:
                names.remove(update)
                names.append(change)
                print(f"{update} changed to {change} successfully.")
                print("-----------------------------------")

        # Delete
        # if select is equal to 4
        elif select == 4:
            print("Delete | List of Names:")
            print("-----------------------------------")
            # Display the List of Names
            for i in names:
                print(i)

            print("-----------------------------------")
            # Create a delete variable
            delete = input(f"{Fore.WHITE}Enter a name: ")
            print("-----------------------------------")

            # deleting the Names in the List that have been inputted delete variable
            names.remove(delete)
            print(f"{delete} deleted successfully.")
            print("-----------------------------------")

        # Throws an error if a user inputted  Invalid number
        else:
            print(f"{Fore.RED}Invalid, Please enter a valid number option")
            print("-----------------------------------")

        # If a user selects an option in the Menu
        # execute
        # then return to the top, keep asking the user select option
        break

