while True:
    user_input = input("Enter what you want (Hell or Heaven): ").lower()

    if user_input == "heaven":
        print("Welcome, now you are in heaven")
        break  # break AFTER printing

    elif user_input == "hell":
        print("Now you are in hell and you can never ever escape this loop.")

    else:
        print("Invalid input. Please enter 'Hell' or 'Heaven'.")