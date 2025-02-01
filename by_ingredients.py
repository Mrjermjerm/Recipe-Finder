

import requests

def get_recipes_by_ingredients(api_key, ingredients):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        'apiKey': api_key,
        'ingredients': ingredients,
        'number': 5
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching recipes:", e)
        return []

def input_ingredients_for_recipes():
    api_key = "68e165a776fc4d5c92d8c3850cfd72f8"  # Replace with your key 

    while True:
        ingredients = input("Enter ingredients separated by commas (or type 'exit' to quit): ").strip()
        
        if ingredients.lower() == 'exit':
            print("Exiting the program.")
            break
        
        ingredients = ', '.join(ingredient.strip() for ingredient in ingredients.split(','))

        if not ingredients:
            print("Invalid input. Please enter at least one ingredient.")
            continue

        recipes = get_recipes_by_ingredients(api_key, ingredients)
        
        if recipes:
            for recipe in recipes:
                line = "-" * 100
                print(line)
                print("Recipe Title:", recipe['title'])
                print("Used Ingredients:", [ingredient['name'] for ingredient in recipe['usedIngredients']])
                print("Link to Recipe:", f"https://spoonacular.com/recipes/{recipe['id']}")
                print()
        else:
            print("No recipes found for the given ingredients.")


input_ingredients_for_recipes()