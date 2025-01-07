import streamlit as st
from database import (
    init_database,
    save_recipe,
    load_recipes,
    save_meal,
    load_meals,
    delete_meal,
    delete_recipe
)
from datetime import date

def test_database_operations():
    print("Starting database tests...")
    
    try:
        # 1. Initialize database
        print("\nTesting database initialization...")
        init_database()
        print("✓ Database initialized successfully")
        
        # 2. Test recipe operations
        print("\nTesting recipe operations...")
        test_recipe = [
            {"food": "Spinach", "quantity": "100 grams"},
            {"food": "Eggs", "quantity": "100 grams"}
        ]
        save_recipe("Test Recipe", test_recipe)
        recipes = load_recipes()
        assert any(r['recipe_name'] == "Test Recipe" for r in recipes)
        print("✓ Recipe save and load successful")
        
        # Get the ID of the test recipe
        test_recipe_id = next(r['id'] for r in recipes if r['recipe_name'] == "Test Recipe")
        
        # 3. Test recipe deletion
        print("\nTesting recipe deletion...")
        delete_recipe(test_recipe_id)
        recipes_after_deletion = load_recipes()
        assert not any(r['id'] == test_recipe_id for r in recipes_after_deletion)
        print("✓ Recipe deletion successful")
        
        # 4. Test meal operations
        print("\nTesting meal operations...")
        test_meal = [
            {"food": "Spinach", "quantity": "100 grams"},
            {"food": "Eggs", "quantity": "100 grams"}
        ]
        save_meal(date.today(), "Breakfast", test_meal)
        meals_df = load_meals()
        assert not meals_df.empty
        print("✓ Meal save and load successful")
        
        # 5. Test meal deletion
        print("\nTesting meal deletion...")
        meal_id = meals_df.iloc[0]['id']
        delete_meal(meal_id)
        updated_meals = load_meals()
        assert len(updated_meals) < len(meals_df)
        print("✓ Meal deletion successful")
        
        print("\nAll tests completed successfully! ✓")
        
    except Exception as e:
        print(f"\n❌ Error during testing: {str(e)}")
        raise e

if __name__ == "__main__":
    test_database_operations() 