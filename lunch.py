
line = "-" * 100

def get_lunch(): 
    
        choice = input("""
        1) Valnilla
        2) Chocolate
        3) Oreo
        4) Strawberry
        What will you have? """)
        
        if choice == "1":
            return get_creamy_peanut_lime_chicken_with_noodles()
        elif choice == "2":
            return get_chicken_quesadillas()
        elif choice == "3":
            return get_chicken_fried_rice()
        elif choice == "4":
            return get_tuscan_chicken_wrap()
        else:
            print("Invalid choice. Please select a number from 1 to 4.")


def get_creamy_peanut_lime_chicken_with_noodles():
    print(f"""
        Creamy Peanut-Lime Chicken With Noodles
        {line}
        Ingredients:
        Kosher salt
        8 oz. thick rice noodles
        1/2 c. no-sugar-added creamy peanut butter
        3 Tbsp. sweet chili sauce
        2 Tbsp. tamari or soy sauce
        1 Tbsp. sriracha
        1/2 tsp. finely grated lime zest
        2 Tbsp. fresh lime juice
        2 Tbsp. vegetable or canola oil
        2 small or 1 large boneless, skinless chicken breasts (about 8 oz.), chopped into 1/2" pieces
        1 small red bell pepper, seeds and ribs removed, thinly sliced
        3 cloves garlic, thinly sliced
        3 scallions, white and green parts separated, thinly sliced
        2 Tbsp. finely chopped peeled ginger
        1/2 c. fresh cilantro leaves
        1/2 c. small fresh basil leaves
        1/3 c. roasted salted peanuts, finely chopped
        Lime wedges, for serving
        {line}
        Directions:
        Step 1
        Bring a medium pot of water to a boil; generously season with salt. Add noodles and stir to prevent sticking. 
        Remove from heat and let soak until tender, 13 to 15 minutes. Drain in a colander and rinse with cold water.
        Step 2
        Meanwhile, in a medium bowl, whisk peanut butter, chili sauce, tamari, sriracha, lime zest, lime juice, 1/4 teaspoon salt, 
        and 1/4 cup warm water until smooth; set aside.
        Step 3
        In a large skillet over medium-high heat, heat oil. Add chicken, season with salt, and cook, stirring often, 
        until lightly golden in spots and almost cooked through, about 4 minutes. Add bell pepper, garlic, white scallion parts, and ginger; 
        season with salt, if needed. Reduce heat to medium and cook, stirring often, until peppers are tender, about 3 minutes more.
        Step 4
        Add noodles to pan and toss well to combine. Remove from heat and add reserved sauce. Toss to coat in sauce.
        Step 5
        Divide noodles among bowls. Top with green scallion parts, cilantro, basil, and peanuts. Serve with lime wedges alongside.
        """)
    

def get_chicken_quesadillas():
    print(f"""
        Chicken Quesadillas
        {line}
        Ingredients:
        6 Tbsp. vegetable oil, divided
        2 bell peppers, thinly sliced
        1/2 onion, thinly sliced
        Kosher salt
        1 lb. boneless skinless chicken breasts, sliced into strips
        1/2 tsp. chili powder
        1/2 tsp. ground cumin
        1/2 tsp. dried oregano
        4 medium flour tortillas
        2 c. shredded Monterey jack
        2 c. shredded cheddar
        1 ripe avocado, sliced
        2 scallions, thinly sliced
        Sour cream, for serving
        {line}
        Directions:
        Step 1
        In a large skillet over medium-high heat, heat 1 tbsp. neutral oil. 
        Add peppers and onion and season with salt. Cook until soft, 5 minutes. Transfer to a plate. 
        Step 2
        Add 1 tbsp. neutral oil to pan and heat over medium-high heat. 
        Add chicken to pan and season with chili powder, cumin, dried oregano, and ½ teaspoon salt. 
        Cook, stirring occasionally, until golden and cooked through, 8 minutes. Transfer to a plate. Wipe out skillet.
        Step 3
        Add 1 tbsp. neutral in skillet. Add 1 flour tortilla to skillet and top half of the tortilla with a heavy sprinkling of both cheeses, 
        ¼ of the cooked chicken mixture, ¼ of the pepper-onion mixture, a few slices of avocado, and a sprinkling of scallions. 
        Fold the other half of the tortilla over and cook, flipping once, until golden, 3 minutes per side. 
        Step 4
        Repeat with remaining oil, tortillas, chicken, pepper-onion mixture, avocado, and scallions to make 4 quesadillas. 
        Step 5
        Slice into wedges and serve with sour cream.
        """)
    
def get_chicken_fried_rice():
    print(f"""
        Chicken Fried Rice
        {line}
        Ingredients
        5 Tbsp. neutral oil, divided
        3 chicken breasts (about 1 1/2 lb.)
        Kosher salt
        Freshly ground black pepper
        1 medium onion, chopped
        2 carrots, peeled and diced
        3 cloves garlic, minced
        1 Tbsp. freshly minced ginger
        4 c. cooked white rice (preferably leftover)
        3/4 c. frozen peas
        3 large eggs, beaten
        3 Tbsp. low-sodium soy sauce
        2 green onions, thinly sliced
        {line}
        Directions:
        Step 1
        Preheat oven to 350°, rack in the middle position.
        Step 2
        In a medium skillet over medium heat, heat 2 tablespoons neutral oil. 
        Season chicken with salt and pepper on both sides, then add to skillet. 
        Cook until golden on both sides, 8 minutes per side. 
        Step 3
        Transfer pan to oven and bake until cooked through, 6-8 minutes longer. 
        Remove from skillet and let rest 5 minutes, then cut into bite-sized pieces.
        Step 4
        To the same skillet, heat 2 tablespoons oil. Add onion and carrots and cook until soft, 
        5 minutes, Add garlic and ginger and cook until fragrant, 1 minute more. 
        Stir in rice and peas and cook until warmed through, 2 minutes.
        Step 5
        Push rice to one side of skillet and add remaining tablespoon oil to other side. 
        Add egg and stir until almost fully cooked, then fold eggs into rice. 
        Add chicken back to skillet with soy sauce and green onions and stir to combine.
        """)

def get_tuscan_chicken_wrap():
    print(f"""
        Tuscan Chicken Wrap
        {line}
        Ingredients
        6 Tbsp. mayonnaise
        3 Tbsp. chopped fresh basil
        2 Tbsp. chopped sun-dried tomatoes
        2 Tbsp. finely grated Parmesan
        1 Tbsp. chopped fresh oregano or 1 tsp. dried oregano
        1 scallion, sliced
        1 clove garlic, grated
        4 (10") flour wraps
        1 1/2 oz. packed baby spinach or arugula (about 1 1/2 c.), divided
        2 c. cooked chopped rotisserie chicken (about 8 oz.), divided
        4 oz. cherry tomatoes, quartered, divided
        4 oz. fresh mozzarella, sliced, divided
        {line}
        Directions:
        Step 1
        In a small bowl, mix mayonnaise, basil, sun-dried tomatoes, 
        Parmesan, oregano, scallion, and garlic until combined.
        Step 2
        Spread one-quarter of mayonnaise mixture onto 1 wrap, leaving a 1" border. 
        Top with one-quarter of spinach, 1/2 cup chicken, 1 ounce cherry tomatoes, and 1 ounce mozzarella. 
        Fold in sides of wrap, then tightly roll bottom of wrap away from you, keeping sides tucked in, until a burrito shape forms. 
        Repeat with remaining mayonnaise mixture, wraps, spinach, chicken, cherry tomatoes, and mozzarella. Slice wraps in half to serve.
        """)


get_lunch()
