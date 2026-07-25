import functions


def main_menu():
        print("======== MENU ========")
        print("1 - Start tracking")
        print("2 - Quit the app")
        print("======================")
        choice = input("What would you like to do? ")
        if choice not in ["1", "2"]:
            print("\n#### ERROR ####")
            print("That is not a valid menu option, please try again!")
            print("###############\n")
        return choice


def start_tracking_menu(choice):
    current_obj = input("\nEnter current task or project: ")
    functions.start_tracking(current_obj)


while True: 
    choice = main_menu()
    if choice == "1":
        start_tracking_menu(choice)
    elif choice == "2":
        break
