

line = "-" * 100
# get dinner
def get_dinner():
    
        choice = input("""
        1) Chicken Curry
        2) Classic, Hearty Beef Stew
        3) Steak and Egg Hash
        4) Steak and Potato Foil Packets               

        What will you have? """)
        if choice == "1":
            return get_chicken_curry()
        elif choice == "2":
            return get_classic_hearty_beef_stew()
        elif choice == "3":
            return get_steak_and_egg_hash()
        elif choice == "4":
            return get_steak_and_potat_foil_packets()
        else:
            print("Invalid choice. Please select a number from 1 to 4.")


def get_chicken_curry():
    print(f"""
        Chicken Curry
        {line}
        Ingredients
        1 large white onion, coarsely chopped
        1 jalapeño, seeded, coarsely chopped
        1 (2 1/2") piece ginger, peeled, coarsely chopped
        8 cloves garlic, peeled
        3 Tbsp. vegetable oil
        2 Tbsp. curry powder
        Kosher salt
        2 Tbsp. tomato paste
        2 c. tomato puree
        2/3 c. whole-milk yogurt
        2 lb. boneless, skinless chicken thighs
        1 tsp. garam masala
        Basmati rice and chopped fresh cilantro, for serving
        {line}
        Directions
        Step 1
        In a food processor, pulse onion until a puree forms. If onions get stuck and don’t process correctly,
        stir with a spoon, cover, and continue to pulse. Transfer onion puree to a small bowl.
        Step 2
        In food processor, pulse jalapeño, ginger, garlic, and 1/2 cup water until a paste forms. 
        Transfer to another small bowl; reserve food processor.
        Step 3
        In a large pot over medium heat, heat oil. Toast curry powder, stirring, until very fragrant, 
        about 1 minute. Add onion puree; season with salt. Cook, stirring occasionally, until mixture loses most of its moisture and becomes a thick paste, 
        about 5 minutes. Add jalapeño mixture and cook, stirring occasionally, until fragrant, about 1 minute. Add tomato paste and cook, stirring frequently, 
        until paste darkens in color, about 2 minutes more.
        Step 4
        Return onion mixture to food processor. Add tomato puree and yogurt. Pulse until sauce is smooth. Return to pot, stir in 1 cup water, and bring to a boil. 
        Reduce heat to low and bring to a gentle simmer.
        Step 5
        Pat chicken dry with paper towels; season all over with salt. Add to pot, cover, and cook, stirring every 5 minutes to ensure nothing sticks to bottom of pot,
        until an instant-read thermometer inserted into thickest part of chicken registers 165°, about 20 minutes; season with salt, if needed. 
        Sprinkle with garam masala and stir to combine.
        Step 6
        Divide rice among bowls. Spoon chicken curry over. Top with cilantro.
        """)


def get_classic_hearty_beef_stew():
    print(f"""
        Classic, Hearty Beef Stew
        {line}
        Ingredients:
        1 (2 pound) boneless beef round steak, cut into 1-inch cubes
        kosher salt and cracked black pepper to taste
        ¼ cup all-purpose flour
        1 tablespoon smoked paprika
        1 tablespoon canola oil
        3 cups chopped onion
        6 cloves garlic, minced
        4 tablespoons tomato paste
        2 cups dry red wine
        1 tablespoon dried thyme
        1 tablespoon dried rosemary
        1 tablespoon herbes de Provence
        3 bay leaves
        2 cups beef broth, or more as needed
        1 tablespoon Worcestershire sauce 
        3 cups chopped carrots
        3 cups cubed Yukon Gold potatoes
        1 cup fresh peas
        1 ½ teaspoons chopped fresh rosemary
        1 teaspoon chopped fresh thyme, or to taste
        {line}
        Directions:
        Step 1
        Gather all ingredients and preheat the oven to 350 degrees F (175 degrees C).
        Step 2
        Season beef with salt and pepper in a large bowl. Add flour and paprika and toss until evenly coated.
        Step3
        Heat oil in a Dutch oven over medium-high heat. Working in batches, sear beef in hot oil, stirring occasionally, until well-browned, 
        10 to 11 minutes per batch. Transfer beef to a plate and leave drippings in the pot.
        Step 4
        Add onion to drippings; season with salt and pepper. Cook and stir until onion begins to caramelize, about 10 minutes. Add garlic and stir until fragrant, about 30 seconds.
        Step 5
        Stir in tomato paste; cook until it turns brown and begins to caramelize and stick to the bottom of the pan.
        Step 6
        Pour in red wine and bring to a boil while scraping the browned bits of food off the bottom of the pan with a wooden spoon. 
        Cook until wine is almost evaporated, about 3 minutes.
        Step 7
        Add thyme, rosemary, herbes de Provence, and bay leaves. Stir in broth and Worcestershire sauce; bring to a boil.
        Step 8
        Return beef to the pot, then remove from heat and cover with the lid.
        Step 9
        Braise stew in the preheated oven until beef is almost tender, about 1 hour 30 minutes. Remove from the oven.
        Step 10
        Add carrots, potatoes, and more beef broth if needed. Cover the pot and return to the oven to braise until beef and vegetables are tender, about 30 minutes more.
        Step 11 
        Discard bay leaves. Stir in peas, rosemary, and thyme. Serve hot.
        """)



def get_steak_and_egg_hash():
    print(f"""
        Steak and Egg Hash
        {line}
        Ingredients:
        1 beef sirloin steak, sliced
        1 pound potatoes, cut into small pieces
        salt and ground black pepper to taste
        1 sweet onion, chopped
        4 Eggland's Best eggs
        1 cup cherry tomatoes, halved
        Italian seasoning
        {line}
        Directions:
        Step 1
        Heat a cast iron skillet over medium heat; add steak and cook 4 to 5 minutes on each side. 
        An instant-read thermometer inserted into the center should read 140 degrees F (60 degrees C) for medium doneness. 
        Remove steak to a plate and reserve the drippings in the skillet.
        Step 2
        Add potatoes to the skillet; season with salt and pepper. Cook, stirring occasionally, until potatoes are just tender, about 8 to 12 minutes.
        Step3
        Add onion and cook until lightly browned and the potatoes are cooked through, about 3 to 5 minutes.
        Step 4
        Slice steak into pieces and return to the skillet, reduce heat to low. Make 4 shallow wells in the potato mixture and crack an egg into each one. 
        Scatter the tomatoes throughout the skillet and cover; cook until the egg whites are set but the yolks are still runny, about 6 to 12 minutes.
        Step 5
        Season eggs with salt, pepper, and Italian Seasoning; serve.
        """)



def get_steak_and_potat_foil_packets():
    print(f"""
        Steak and Potato Foil Packets
        {line}
        Ingredients:
        1 pound small Yukon Gold potatoes, halved
        1 1/2 pounds sirloin steak, cut into bite-sized strips
        1 yellow onion, sliced 
        1 red bell pepper, sliced
        1 green bell pepper, sliced
        1 carrot, thinly sliced 
        4 tablespoons butter, or as needed 
        1 teaspoon steak seasoning, or as needed
        5 cloves garlic, chopped, or more to taste
        {line}
        Directions:
        Step 1
        Prepare an outdoor grill, preferably a charcoal grill, for medium-high heat.
        Step 2
        Place potatoes in a microwave-safe dish and cook on high until they are tender with a bite, about 3 minutes.
        Step3
        Divide steak, potatoes, onions, red and green bell pepper, and carrots evenly onto 4 to 6 squares of aluminum foil. 
        Add 1 tablespoon butter and a little fresh garlic to each pack; fold foil over the top to close each packet tightly.
        Step 4
        Place foil packs on the hot side of the grill. Cook for 5 minutes. Carefully open one foil pack to check for steak doneness.
        Step 5
        If steak is not cooked to your taste after 5 minutes, continue to cook, checking for doneness every few minutes. 
        An instant-read thermometer inserted into the center will read 130 degrees F (54 degrees C) for medium rare.
        """)


get_dinner()