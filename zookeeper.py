from os import system, name
from animals import animals


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


choice = ""

while choice != "exit":
    choice = input(
        "Please enter the number of the habitat you would like to view, type 'exit' if you want to exit: ").lower()
    if choice != "exit":
        try:
            clear()
            print(animals[int(choice)])
            print()
        except(ValueError, IndexError) as error:
            if type(error) == ValueError:
                print("\nError! You did not enter a number")
            elif type(error) == IndexError:
                print("\nError! Index out of range")
            print("Please enter a number between 0 to 5\n")
    else:
        clear()
        print("See you later!")
