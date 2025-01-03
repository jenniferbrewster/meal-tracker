import streamlit as st
from Meals import check_password, load_recipes, save_recipe, get_all_foods_with_categories, ALLOWED_FOODS, RECIPES_FILE
import json

if not check_password():
    st.stop()

st.title("Recipes")

# Initialize session state for recipe creation
if 'recipe_foods' not in st.session_state:
    st.session_state.recipe_foods = []

if 'food_item_reset' not in st.session_state:
    st.session_state.food_item_reset = False

if 'editing' not in st.session_state:
    st.session_state.editing = False

if 'editing_recipe_name' not in st.session_state:
    st.session_state.editing_recipe_name = ""

def reset_food_fields():
    """Reset only the food and quantity input fields."""
    st.session_state.food_item_reset = True
    if 'quantity' in st.session_state:
        del st.session_state.quantity

def add_food_to_recipe(foods_list, food_item, quantity):
    """Add a food item and its quantity to the recipe."""
    if not food_item or food_item == "":
        st.error("Please select a food item")
        return False
    if not quantity or quantity.strip() == "":
        st.error("Please enter a quantity")
        return False
    
    foods_list.append({"food": food_item, "quantity": quantity})
    st.success(f"Added {food_item} to recipe")
    return True

def delete_recipe(recipe_name):
    """Delete a recipe from the recipes file."""
    recipes = load_recipes()
    if recipe_name in recipes:
        del recipes[recipe_name]
        with open(RECIPES_FILE, 'w') as f:
            json.dump(recipes, f)
        st.success(f"Recipe '{recipe_name}' deleted successfully!")
        st.rerun()

def edit_recipe(recipe_name):
    """Load a recipe into edit mode."""
    recipes = load_recipes()
    if recipe_name in recipes:
        st.session_state.recipe_foods = recipes[recipe_name]
        st.session_state.editing_recipe_name = recipe_name
        st.session_state.editing = True
        st.session_state.food_item_reset = True

def update_recipe(recipe_name, foods):
    """Update an existing recipe with new foods."""
    recipes = load_recipes()
    recipes[recipe_name] = foods
    with open(RECIPES_FILE, 'w') as f:
        json.dump(recipes, f)
    st.success(f"Recipe '{recipe_name}' updated successfully!")

# Recipe Creation Section
st.header("Create/Edit Recipe")
if st.session_state.editing:
    recipe_name = st.session_state.editing_recipe_name
    st.write(f"Editing Recipe: {recipe_name}")
else:
    recipe_name = st.text_input("Recipe Name:", key="recipe_name")

# Get all foods with their categories
foods_dict = get_all_foods_with_categories()
all_foods = list(foods_dict.keys())

# Handle food item selection
if st.session_state.food_item_reset:
    food_item = st.selectbox(
        "Enter food item:",
        options=[""] + all_foods,
        format_func=lambda x: x,
        placeholder="Start typing to search foods...",
        key="recipe_food_item",
        index=0
    )
    st.session_state.food_item_reset = False
else:
    food_item = st.selectbox(
        "Enter food item:",
        options=[""] + all_foods,
        format_func=lambda x: x,
        placeholder="Start typing to search foods...",
        key="recipe_food_item"
    )

# Show quantity input and add button
if food_item:
    quantity = st.text_input("Enter quantity (in grams):", key="quantity")
    if st.button("Add Food to Recipe"):
        if add_food_to_recipe(st.session_state.recipe_foods, food_item, quantity):
            reset_food_fields()
            st.rerun()

# Display current foods in recipe
if st.session_state.recipe_foods:
    st.write("Current foods in recipe:")
    for i, food in enumerate(st.session_state.recipe_foods):
        col1, col2 = st.columns([6, 1])
        with col1:
            st.write(f"- {food['food']}: {food['quantity']}")
        with col2:
            if st.button("❌", key=f"remove_food_{i}"):
                st.session_state.recipe_foods.pop(i)
                st.rerun()

    # Save/Update Recipe button
    if st.session_state.editing:
        if st.button("Update Recipe"):
            update_recipe(st.session_state.editing_recipe_name, st.session_state.recipe_foods)
            st.session_state.recipe_foods = []
            st.session_state.editing = False
            st.session_state.editing_recipe_name = ""
            st.rerun()
    else:
        if recipe_name and st.button("Save Recipe"):
            save_recipe(recipe_name, st.session_state.recipe_foods)
            st.session_state.recipe_foods = []
            st.rerun()

    # Cancel Edit button (only show when editing)
    if st.session_state.editing:
        if st.button("Cancel Edit"):
            st.session_state.recipe_foods = []
            st.session_state.editing = False
            st.session_state.editing_recipe_name = ""
            st.rerun()
    
    # Clear Recipe button
    if st.button("Clear Recipe"):
        st.session_state.recipe_foods = []
        if st.session_state.editing:
            st.session_state.editing = False
            st.session_state.editing_recipe_name = ""
        st.rerun()

# Modify the Existing Recipes section to use a callback
def handle_edit_click(recipe_name):
    st.session_state.editing = True
    st.session_state.editing_recipe_name = recipe_name
    st.session_state.recipe_foods = load_recipes()[recipe_name]
    st.session_state.food_item_reset = True

# Existing Recipes Section
st.header("Existing Recipes")
recipes = load_recipes()

if recipes:
    for recipe_name, foods in recipes.items():
        col_recipe, col_edit, col_delete = st.columns([5, 1, 1])
        with col_recipe:
            with st.expander(recipe_name):
                for food in foods:
                    st.write(f"- {food['food']}: {food['quantity']}")
        with col_edit:
            # Use on_click callback instead of checking button return value
            st.button("✏️", 
                     key=f"edit_{recipe_name}", 
                     on_click=handle_edit_click,
                     args=(recipe_name,))
        with col_delete:
            if st.button("🗑️", key=f"delete_{recipe_name}"):
                delete_recipe(recipe_name)
                st.rerun()
else:
    st.write("No recipes saved yet.") 