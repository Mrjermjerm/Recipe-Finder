


def get_breakfast():
    while True:
        choice = input("""
        1) 

        What will you have? """)
        if choice == "1":
            return get()
        elif choice == "2":
            return get_()
        elif choice == "3":
            return get_()
        elif choice == "4":
            return get_()
        else:
            print("Invalid choice. Please select a number from 1 to 4.")


def get():
    line = "-" * 100
    print(f"""

        {line}
        Ingredients

        {line}
        Directions

""")




get_breakfast()