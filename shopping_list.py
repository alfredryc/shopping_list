
import os
EXIT = "exit"
NAME_FILE = "shopping_list.txt"
# Products available
super_items = ["bread", "egg", "cheese"]


def ask_the_user():
    return input("What to buy or type ({}) type ({}) To exit): ".format(super_items, EXIT)) 

def save_list(buy_list):
    with open(NAME_FILE, "w") as f:  
        f.write("\n".join(buy_list))


def save_item(buy_list, item_save):
     if item_save in [a.lower() for a in buy_list]:
         print("The product already exists.")
     
     else:
        buy_list.append(item_save)
        show_list(buy_list)

def load_create_file():

    buy_list = []

    if input("Do you want to load the previous list? (y/n): ") == "y":
        try:
            with open(NAME_FILE, "r") as f:
                # Save the content in the list
                buy_list = f.read().split("\n")
                #buy_list = f.read().splitlines()
                print("\n".join(buy_list))

        except FileNotFoundError:
            print("File not found")
    return buy_list

def show_list(buy_list):
    print("\n".join(buy_list))
    return buy_list


def main():
    buy_list = load_create_file()
    show_list(buy_list)
    input_user = ask_the_user()

    while input_user != EXIT:

        save_item(buy_list, input_user)
        input_user = ask_the_user()

    show_list(buy_list)
    save_list(buy_list)
         
if __name__ == "__main__":
    main()
