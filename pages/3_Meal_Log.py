import streamlit as st
import pandas as pd
from Meals import load_data, delete_meal, format_foods_for_display

st.title("Meal Log")

# Load data
data = load_data()
if not data.empty:
    # Create meal type order mapping
    meal_order = {
        "Breakfast": 1,
        "Snack": 2,
        "Lunch": 3,
        "Dinner": 4
    }
    
    # Add meal order column for sorting
    data['meal_order'] = data['meal_type'].map(meal_order)
    
    # Sort by date (descending) and meal order
    data = data.sort_values(['date', 'meal_order'], ascending=[False, True])
    
    # Remove the meal_order column as we don't need it for display
    data = data.drop('meal_order', axis=1)

# Filter by date
filter_date = st.date_input("Filter by date (optional):", value=None, key="filter_date")

# Create a scrollable container with fixed height
meal_log_container = st.container()
with meal_log_container:
    if filter_date:
        filtered_data = data[data["date"] == filter_date.isoformat()].copy()
        if not filtered_data.empty:
            # Sort filtered data by meal type
            meal_order = {"Breakfast": 1, "Snack": 2, "Lunch": 3, "Dinner": 4}
            filtered_data["meal_order"] = filtered_data["meal_type"].map(meal_order)
            filtered_data = filtered_data.sort_values("meal_order")
            filtered_data = filtered_data.drop('meal_order', axis=1)
            filtered_data["foods"] = filtered_data["foods"].apply(format_foods_for_display)
            
            st.write(f"Meals on {filter_date.isoformat()}:")
            
            # Display meals
            for _, row in filtered_data.iterrows():
                col1, col2, col3 = st.columns([2, 6, 1])
                with col1:
                    st.write(row["meal_type"])
                with col2:
                    st.write(row["foods"])
                with col3:
                    if st.button("❌", key=f"delete_{row['id']}"):
                        delete_meal(row['id'])
        else:
            st.write("No meals logged for this date.")
    else:
        st.write("All recorded meals:")
        display_data = data.copy()
        display_data["foods"] = display_data["foods"].apply(format_foods_for_display)
        
        # Display all meals
        for _, row in display_data.iterrows():
            col1, col2, col3, col4 = st.columns([2, 2, 6, 1])
            with col1:
                st.write(row["date"])
            with col2:
                st.write(row["meal_type"])
            with col3:
                st.write(row["foods"])
            with col4:
                if st.button("🗑️", key=f"delete_{row['id']}"):
                    delete_meal(row['id']) 