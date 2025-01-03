import streamlit as st
from food_data import ALLOWED_FOODS

st.title("Allowed Foods Reference")

# Function to format portion and conversion info
def format_food_info(food_info):
    if isinstance(food_info, dict):
        portion = food_info['portion']
        conversion = food_info.get('conversion')
        
        # Format portion info
        portion_text = f"**Portion:** {portion}"
        
        # Add conversion info if available
        if conversion:
            return f"{portion_text}\n\n*{conversion}*"
        return portion_text
    return f"**Portion:** {food_info}"

# Display allowed foods by category
for category, foods in ALLOWED_FOODS.items():
    st.header(category)
    
    # Special note for Fruits category
    if category == 'Fruits':
        st.write("**Note:** Maximum 2 portions of listed fruits per day (except lemon and lime)")
    
    # Create columns for better organization
    cols = st.columns(2)
    
    # Split foods into two columns
    foods_list = list(foods.items())
    mid_point = len(foods_list) // 2
    
    # First column
    with cols[0]:
        for food_name, food_info in foods_list[:mid_point]:
            with st.expander(food_name):
                st.markdown(format_food_info(food_info))
    
    # Second column
    with cols[1]:
        for food_name, food_info in foods_list[mid_point:]:
            with st.expander(food_name):
                st.markdown(format_food_info(food_info))
    
    # Add some space between categories
    st.markdown("---") 