
line = "-" * 100

def get_smoothies(): 
    
        choice = input("""
        1) Valnilla
        2) Chocolate
        3) Oreo
        4) Strawberry
        What will you have? """)
        
        if choice == "1":
            return get_strawberry_banana_smoothie()
        elif choice == "2":
            return get_mixed_berry_smoothie()
        elif choice == "3":
            return get_orange_julius()
        elif choice == "4":
            return get_banana_pudding_milkshake()
        else:
            print("Invalid choice. Please select a number from 1 to 4.")


def get_strawberry_banana_smoothie():
    print(f"""
        Strawberry Banana Smoothie
        {line}
        Ingredients:
        1½ cups raspberries
        1 cup strawberries
        ½ frozen banana
        1 cup almond milk or oat milk, plus more as needed
        1 tablespoon honey or maple syrup, plus more to taste
        Handful fresh basil or mint, optional
        1½ cups ice
        {line}
        Directions:
        Step 1
        Combine the raspberries, strawberries, banana, almond milk, honey, basil, 
        if using, and ice in a blender. Blend until smooth.
        Step 2
        Taste. If it's too tart for you, add more almond milk and/or honey as desired.
        Optional
        Optional step, strain to remove seeds: Blend all ingredients except ice. 
        Strain the liquid to remove strawberry seeds, return to blender, add ice and pulse until combined.
        """)


def get_mixed_berry_smoothie():
    print(f"""
        Mixed Berry Smoothie
        {line}
        Ingredients:
        3 cups frozen mixed berries ($4.99)
        1 frozen banana, sliced ($0.21)
        1/2 cup plain yogurt ($0.80)
        1/2 tsp vanilla extract ($0.25)
        1 Tbsp sugar ($0.02)
        1 1/2 cups unsweetened almond milk* ($0.65)
        {line}
        Directions:
        Step 1
        Add the frozen mixed berries, frozen banana (sliced in half), yogurt, 
        vanilla extract, sugar, and almond milk to a large blender.
        Step 2
        Blend the ingredients until smooth. If the smoothie is too thick, 
        add more milk as needed to make it blend smoothly. Serve immediately and enjoy.
        """)


def get_orange_julius():
    print(f"""
        Orange Julius
        {line}
        Ingredients:
        1/2 cup frozen orange juice concentrate ($1.16)
        1 cup whole milk ($0.20)
        1 tsp vanilla extract ($0.45)
        3 Tbsp granulated sugar ($0.06)
        1 cup ice ($0.00)
        {line}
        Directions:
        Place all of the ingredients in a blender and blend until smooth and frothy.
        If your Orange Julius is not thick enough, add more ice. 
        If the Julius is too thick, add a little water or milk and blend again until you reach the desired consistency. 
        Serve immediately and enjoy!
        """)


def get_banana_pudding_milkshake():
    print(f"""
        Orange Julius
        {line}
        Ingredients:
        1 cup 1% milk
        2 cups vanilla frozen yogurt
        1 banana, divided 
        1 (.9 ounce) package sugar-free banana cream pudding mix
        1/2 cup vanilla wafers, divided
        {line}
        Directions:
        Step 1
        Add milk and frozen yogurt to the jar of a blender. Slice banana; set 4 to 6 slices aside for garnish. 
        Add remaining banana and pudding mix to the blender. Set 2 vanilla wafers aside for garnish; 
        add remaining vanilla wafers to the blender. Blend until smooth.
        Step 2
        Pour mixture into 2 tall glasses. Top each milkshake with whipped cream, remaining banana slices, and a vanilla wafer.
        Step 3
        """)


get_smoothies()