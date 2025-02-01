

from pushbullet import Pushbullet 
import random
import string
import time


# Recipe account, with password authintication

def main(): 

    print('Please create account with Pushbullet. ') 
    print('Link your phone for messaging.\n')

    create_random_password() # Creates random password 
    message() # Sends password to users phone
    check_password() # Checks users input for correct password


    while True:   
        choice = input(f"""
        1) Milk Shakes
        2) Smoothies
        3) Breakfast
        4) Lunch
        5) Dinner
        6) By Ingridents 
        Please select an option: """)

        if choice == "1":
            from milkshakes import get_milkshakes
            milkshake = get_milkshakes
            return milkshake
        
        elif choice == "2":
            from smoothies import  get_smoothies
            smoothies = get_smoothies
            return smoothies
        
        elif choice == "3":
            from breakfast import get_breakfast
            breakfast = get_breakfast
            return breakfast
        
        elif choice == "4":
            from lunch import get_lunch
            lunch = get_lunch
            return lunch
        
        elif choice == "5":
            from dinner import get_dinner
            dinner = get_dinner
            return dinner
        
        elif choice == '6':
            from by_ingredients import input_ingredients_for_recipes
            ingredients = input_ingredients_for_recipes
            return ingredients
        
        else:
            print("\nInvalid choice. Please select a number from 1 to 5.\n")
            time.sleep(1)



# Random passoword generated
def create_random_password():
    length = 5
    characters = string.ascii_letters + string.digits
    password = ''

    for _ in range(length):
        password += random.choice(characters)

    with open("password.txt", "w") as password_file:
        password_file.write(password)
    return password



# Sends password to users phone
def message():
    def send_pushbullet(message):
        access_token = "o.oWkZ3rjqFbmGhKC3eFD9osA8WxlrzHJW"
        pb = Pushbullet(access_token)

        # Send a notification
        pb.push_note("Notification", message)
        print("A unique password has been sent.\n")

    send_pushbullet(create_random_password())



# Read the password from the file
def read_password():
    try:
        with open("password.txt", "r") as password_file:
            password = password_file.read().strip()
        return password
    except FileNotFoundError:
        print("Password file not found. Please create a password first.")
        return None



# Check if password matches when being inputed by user
def check_password():
    with open("password.txt", "r") as password_file:
        enter = input("Enter password: ")
        for password in password_file:
            if enter == read_password():
                print("Password accepted:")
                break  
            else:
                print("Incorrect password.")



if __name__=="__main__":
    main()