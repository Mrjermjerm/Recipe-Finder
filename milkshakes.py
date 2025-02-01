

# Get Milkshake
def get_milkshakes():
    
        choice = input("""
        1) Valnilla
        2) Chocolate
        3) Oreo
        4) Strawberry
        What will you have? """)
        if choice == "1":
            return get_vanilla_shake()
        elif choice == "2":
            return get_choclate_shake()
        elif choice == "3":
            return get_oreo_shake()
        elif choice == "4":
            return get_straberry_shake()
        else:
            print("Invalid choice. Please select a number from 1 to 4.")

# Vanilla
def get_vanilla_shake():
    line = "-" * 100
    print(f"""
        Vanilla Milkshake
        {line}
        Ingredients:
        2 cups vanilla ice cream
        1 cup whole milk 
        1 teaspoon vanilla extract
        {line}
        Directions:
        Step 1:
        Blend ice cream, milk, and vanilla extract together in a blender until smooth.
        Step 2:
        Enjoy!!
        """)

# Choclate
def get_choclate_shake():
    line = "-" * 100
    print(f"""
        Chocolate Milkshake
        {line}
        Ingredients:
        2 cups vanilla ice cream
        1/2 cup whole milk, cold
        1/4 cup chocolate syrup
        1/4 cup chocolate chips, optional
        Whipped cream, garnish
        Shaved chocolate, garnish
        {line}
        Directions:
        Step 1:
        Place the ice cream, milk, and chocolate syrup into the blender. 
        If using chocolate chips, add those as well. 
        Be mindful that the harder the ice cream is, the better, 
        as the blending process can liquefy the ice cream too much and make the milkshake too thin.
        Step 2:
        Blend the ingredients until completely smooth.
        """)

# Oreo
def get_oreo_shake():
    line = "-" * 100
    print(f"""
        Oreo Milkshake
        {line}
        Ingredients:
        1 pint vanilla ice cream
        1 cup milk (preferably whole milk)
        8 Oreo cookies (or other chocolate sandwich cookies)
        1 tablespoon chocolate sauce
        2 Oreo cookies, garnish
        {line}
        Directions:
        Step 1:
        Place 1 pint vanilla ice cream, 1 cup milk, 8 Oreo cookies, 
        and 1 tablespoon chocolate sauce in a blender and puree until smooth
        Step2:
        Crush the remaining 2 Oreo cookies for the garnish by placing them in a zip-close plastic bag 
        and pounding on them a few times with a rolling pin until they crumble.
        """)

# Strawberry
def get_straberry_shake():
    line = "-" * 100
    print(f"""
        Strawberry Milkshake
        {line}
        Ingredients:
        1/2 pound fresh strawberries
        1 tablespoon sugar
        1 teaspoon vanilla extract
        1 pint vanilla ice cream
        1/2 cup milk
        Small whole strawberries, garnish
        {line}
        Directions:
        Step 1:
        In a medium bowl, combine the sliced strawberries, sugar, and vanilla extract and stir to combine well.
        Step 2:
        Set aside and allow to sit for at least 20 minutes and for up to 1 hour.
        Step 3:
        Blend all ingredients.
        """)



get_milkshakes()