from animals import animals


while True:
    choice = input(
        "Please enter the number of the habitat you would like to view, type 'exit' if you want to exit: ")
    if choice == "exit":
        print("See you later!")
        break
    # elif choice in ['0', '1', '2', '3', '4', '5']:
        # print(animals[int(choice)])
    else:
      try:
        print(animals[int(choice)])
      except (TypeError, IndexError) as error:
        print("Please enter a number between 0 to 5")
