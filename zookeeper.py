from animals import animals


while True:
    choice = input(
        "Please enter the number of the habitat you would like to view, type 'exit' if you want to exit: ")
    if choice == "exit":
        print("See you later!")
        break
    else:
        try:
            print(animals[int(choice)])
            print()
        except (TypeError, IndexError) as error:
            print("Error! Please enter a number between 0 to 5\n")
