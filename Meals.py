import datetime
import streamlit as st
import pandas as pd
from datetime import date
import json
from food_data import ALLOWED_FOODS, DAILY_FRUIT_PORTION_LIMIT, is_limited_fruit
import logging
import hmac
from database import (
    init_database,
    load_recipes as db_load_recipes,
    load_meals,
    save_meal,
    delete_meal as db_delete_meal
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set page title
st.title("Daily Meal Tracker")

if 'food_item_reset' not in st.session_state:
    st.session_state.food_item_reset = False

if 'current_foods' not in st.session_state:
    st.session_state.current_foods = []

if 'recipe_loaded' not in st.session_state:
    st.session_state.recipe_loaded = False

def reset_form_fields():
    """Reset all form fields to their default states."""
    st.session_state.current_foods = []
    st.session_state.recipe_loaded = False
    st.session_state.food_item_reset = True  # Set flag to reset food item
    if 'recipe_select' in st.session_state:
        del st.session_state.recipe_select
    if 'quantity' in st.session_state:
        del st.session_state.quantity
    if 'recipe_name' in st.session_state:
        del st.session_state.recipe_name

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets.passwords and \
           st.session_state["password"] == st.secrets.passwords[st.session_state["username"]]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password
        st.sidebar.text_input("Username", key="username")
        st.sidebar.text_input("Password", type="password", key="password")
        st.sidebar.button("Login", on_click=password_entered)
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error
        st.sidebar.text_input("Username", key="username")
        st.sidebar.text_input("Password", type="password", key="password")
        st.sidebar.button("Login", on_click=password_entered)
        st.sidebar.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct
        return True

def require_auth(func):
    """Decorator to require authentication before accessing a function"""
    def wrapper(*args, **kwargs):
        if check_password():
            return func(*args, **kwargs)
        else:
            st.stop()  # Stop execution if not authenticated
    return wrapper

# Initialize database on startup
init_database()

# Replace file operations with database calls
@require_auth
def load_data():
    """Load the meal data from the database"""
    return load_meals()

def is_valid_food(food_item):
    """Check if the food item is in the allowed foods list."""
    food_item = food_item.lower()
    for category, foods in ALLOWED_FOODS.items():
        if category == 'Proteins':
            if any(protein.lower() in food_item for protein in foods.keys()):
                return True, category
        else:
            if any(allowed_food.lower() in food_item for allowed_food in foods.keys()):
                return True, category
    return False, None

def add_food_to_meal(foods_list, food_item, quantity):
    """Add a food item and its quantity to the foods list."""
    if not food_item or food_item == "":
        st.error("Please select a food item")
        return False
    if not quantity or quantity.strip() == "":
        st.error("Please enter a quantity")
        return False
        
    is_allowed, category = is_valid_food(food_item)
    if is_allowed:
        foods_list.append({"food": food_item, "quantity": quantity})
        st.success(f"Added {food_item} to meal")
        return True
    else:
        st.error("This food is not in the allowed foods list. Please check the allowed foods section.")
    return False

@require_auth
def add_meal(meal_date, meal_type, foods_list):
    """Add a complete meal to the database"""
    if not foods_list:
        st.error("Please add at least one food item to the meal")
        return load_data()
    
    save_meal(meal_date, meal_type, foods_list)
    st.success(f"{meal_type} added successfully!")
    return load_data()

def format_foods_for_display(foods_str):
    """Convert the JSON string of foods into a readable format."""
    foods = json.loads(foods_str)
    return ", ".join([f"{food['food']}: {food['quantity']}" for food in foods])

@require_auth
def delete_meal(meal_id):
    """Delete a meal from the database"""
    try:
        db_delete_meal(meal_id)
        st.success("Meal deleted successfully!")
    except Exception as e:
        st.error(f"Error deleting meal: {str(e)}")
    finally:
        st.rerun()

def get_all_foods():
    """Get a flat list of all allowed foods."""
    foods = []
    for category, items in ALLOWED_FOODS.items():
        if category != 'Proteins':  # Handle proteins separately as they're all unlimited
            foods.extend(items.keys())
    return sorted(foods)

def get_all_foods_with_categories():
    """Get a flat list of all allowed foods with their categories."""
    foods_dict = {}
    for category, items in ALLOWED_FOODS.items():
        for food in items.keys():
            foods_dict[food] = category
    return foods_dict

@require_auth
def load_recipes():
    """Load recipes from the database"""
    try:
        return db_load_recipes()  # Use the renamed function
    except Exception as e:
        logger.error(f"Error loading recipes: {str(e)}")
        return {}

def load_recipe(recipe_name):
    """Load a recipe's foods into the current meal."""
    recipes = load_recipes()  # This now uses the correct function
    return recipes.get(recipe_name, [])

def reset_food_fields():
    """Reset only the food and quantity input fields."""
    st.session_state.food_item_reset = True
    if 'quantity' in st.session_state:
        del st.session_state.quantity

def get_daily_totals(date):
    """Calculate total grams consumed for each food on a given date."""
    daily_totals = {}
    filtered_data = data[data["date"] == date.isoformat()]
    
    for _, row in filtered_data.iterrows():
        foods = json.loads(row["foods"])
        for food in foods:
            food_name = food["food"]
            # Extract the number from "X grams"
            grams = int(food["quantity"].split()[0])
            if food_name in daily_totals:
                daily_totals[food_name] += grams
            else:
                daily_totals[food_name] = grams
    
    return daily_totals

def get_total_fruit_portions(date):
    """Calculate total fruit portions consumed for a given date across all fruits."""
    total_portions = 0 
    filtered_data = data[data["date"] == date.isoformat()]
       
    for _, row in filtered_data.iterrows():
        foods = json.loads(row["foods"])
        for food in foods:
            food_name = food["food"]
            # Skip lemons and limes
            if food_name in ["lemon", "lime"]:
                continue
            
            # Check if this is a fruit
            for category, foods_dict in ALLOWED_FOODS.items():
                if (category == "Fruits"): 
                        for food in foods_dict.items():
                            if food[0] == food_name:  
                                total_portions +=1
    
    return total_portions

def check_portion_limits(food_name, quantity_grams, date):
    """Check if adding this food would exceed any limits."""
    category = foods_dict[food_name]
    food_info = ALLOWED_FOODS[category][food_name]
    
    warnings = []
    
    # Check per-meal limit
    if 'max_per_meal' in food_info and food_info['max_per_meal']:
        if quantity_grams > food_info['max_per_meal']:
            warnings.append(f"⚠️ Exceeds meal limit of {food_info['max_per_meal']}g per meal")
    
    # Check daily limit
    if 'max_per_day' in food_info and food_info['max_per_day']:
        daily_totals = get_daily_totals(date)
        current_total = daily_totals.get(food_name, 0)
        if current_total + quantity_grams > food_info['max_per_day']:
            warnings.append(f"⚠️ Exceeds daily limit of {food_info['max_per_day']}g per day")
    
    # Check combined fruit portion limit
    if is_limited_fruit(food_name, category):
        current_portions = get_total_fruit_portions(date)
        print(current_portions)
        if current_portions > DAILY_FRUIT_PORTION_LIMIT:
            warnings.append(f"⚠️ Exceeds daily limit of {DAILY_FRUIT_PORTION_LIMIT} total fruit portions per day")
    
    return warnings

# Load existing data at the start
data = load_data()
recipes = load_recipes()

# Section: Add a new meal
st.header("Log a New Meal")

# Create columns for the meal input
col1, col2 = st.columns(2)

with col1:
    meal_date = st.date_input("Select the date:", 
                             value=date.today(),
                             key="meal_date_input")
    meal_type = st.selectbox("Select meal type:", 
                            ["Breakfast", "Lunch", "Dinner", "Snack"],
                            key="meal_type_select")
    
    # Move Save Complete Meal button here
    if st.session_state.current_foods:
        if st.button("Save Complete Meal"):
            add_meal(meal_date, meal_type, st.session_state.current_foods)
            reset_form_fields()
            st.rerun()
    
    # Recipe loading option (removed the recipes loading from here)
    if recipes and not st.session_state.recipe_loaded and not st.session_state.current_foods:
        st.write("Load foods from recipe (if applicable):")
        # Extract recipe names from the list of dictionaries
        recipe_names = [recipe['recipe_name'] for recipe in recipes]
        selected_recipe = st.selectbox("Select recipe:", [""] + recipe_names, key="recipe_select")
        if selected_recipe:
            # Find the selected recipe in the list
            selected_recipe_data = next((recipe for recipe in recipes if recipe['recipe_name'] == selected_recipe), None)
            if selected_recipe_data:
                st.session_state.current_foods = selected_recipe_data['foods']
                st.session_state.recipe_loaded = True
                st.rerun()

# Add food items to the meal
with col2:
    st.write("Add foods to your meal:")
    
    # Get all foods with their categories
    foods_dict = get_all_foods_with_categories()
    all_foods = list(foods_dict.keys())
    
    # Handle food item reset
    if st.session_state.food_item_reset:
        # Instead of modifying food_item directly, we'll use the index parameter
        food_item = st.selectbox(
            "Enter food item:",
            options=[""] + all_foods,
            format_func=lambda x: x,
            placeholder="Start typing to search foods...",
            key="food_item",
            index=0  # This will select the empty option
        )
        st.session_state.food_item_reset = False
    else:
        food_item = st.selectbox(
            "Enter food item:",
            options=[""] + all_foods,
            format_func=lambda x: x,
            placeholder="Start typing to search foods...",
            key="food_item"
        )
    
    # Show the allowed portion for the selected food
    quantity_number = st.number_input("Grams:", min_value=0, step=1, key="quantity_number")
    
    if food_item:
        category = foods_dict[food_item]
        food_info = ALLOWED_FOODS[category][food_item]
        allowed_portion = food_info['portion']
        conversion_info = food_info.get('conversion')
        
        # Color code the portion display
        if 'Unlimited' in allowed_portion:
            st.markdown(f'<p style="color:green">Allowed portion: {allowed_portion}</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="color:orange">Allowed portion: {allowed_portion}</p>', unsafe_allow_html=True)
        
        # Display conversion information if available
        if conversion_info:
            st.info(conversion_info)
        
        if st.button("Add Food to Meal"):
            quantity = f"{quantity_number} grams"
            
            # Check portion limits before adding
            warnings = check_portion_limits(food_item, quantity_number, meal_date)
            if warnings:
                for warning in warnings:
                    st.warning(warning)
            
            if add_food_to_meal(st.session_state.current_foods, food_item, quantity):
                reset_food_fields()
                st.rerun()
    
    # Display current foods in the meal with any limit warnings
    if st.session_state.current_foods:
        st.markdown("---")
        st.write("Current foods in this meal:")
        for food in st.session_state.current_foods:
            st.write(f"- {food['food']}: {food['quantity']}")
            # Check current limits
            grams = int(food['quantity'].split()[0])
            warnings = check_portion_limits(food['food'], grams, meal_date)
            for warning in warnings:
                st.warning(warning)
        
        # Move Clear Current Meal button here
        if st.button("Clear Current Meal"):
            reset_form_fields()
            st.rerun()
