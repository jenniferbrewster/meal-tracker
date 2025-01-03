import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from Meals import load_data
from food_nutrients import FOOD_NUTRIENTS
import json

st.title("Nutrient Analysis")

# Load meal data
data = load_data()

def calculate_nutrients(foods_list):
    """Calculate total nutrients for a list of foods."""
    total_nutrients = {
        'calories': 0,
        'protein': 0,
        'fat': 0,
        'carbs': 0,
        'fiber': 0
    }
    
    for food in foods_list:
        food_name = food['food']
        print(food['food'])
        grams = float(food['quantity'].split()[0])
        
        # Find the food in FOOD_NUTRIENTS
        for category in FOOD_NUTRIENTS.values():
            if food_name in category:
                nutrients = category[food_name]
                # Calculate nutrients based on grams (nutrients are per 100g)
                multiplier = grams / 100
                for nutrient in total_nutrients:
                    total_nutrients[nutrient] += nutrients[nutrient] * multiplier
                break              
    return total_nutrients

# Date range selector
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", value=datetime.now().date() - timedelta(days=7))
with col2:
    end_date = st.date_input("End Date", value=datetime.now().date())

# Filter data by date range
mask = (pd.to_datetime(data['date']).dt.date >= start_date) & (pd.to_datetime(data['date']).dt.date <= end_date)
filtered_data = data[mask].copy()

if not filtered_data.empty:
    # Calculate daily nutrients
    daily_nutrients = {}
    
    for _, row in filtered_data.iterrows():
        date = row['date']
        foods = json.loads(row['foods'])
        nutrients = calculate_nutrients(foods)
        
        if date not in daily_nutrients:
            daily_nutrients[date] = {
                'calories': 0,
                'protein': 0,
                'fat': 0,
                'carbs': 0,
                'fiber': 0
            }
        
        for nutrient in nutrients:
            daily_nutrients[date][nutrient] += nutrients[nutrient]
    
    # Create DataFrame for plotting
    df_nutrients = pd.DataFrame.from_dict(daily_nutrients, orient='index')
    df_nutrients.index = pd.to_datetime(df_nutrients.index)
    
    # Create tabs for different visualizations
    tab1, tab2, tab3 = st.tabs(["Daily Macronutrients", "Daily Calories", "Average Macronutrient Ratios"])
    
    with tab1:
        st.subheader("Macronutrients Per Day")
        fig = go.Figure()
        for nutrient in ['protein', 'fat', 'carbs', 'fiber']:
            fig.add_trace(go.Bar(
                name=nutrient.capitalize(),
                x=df_nutrients.index,
                y=df_nutrients[nutrient],
            ))
        fig.update_layout(barmode='stack')
        st.plotly_chart(fig)
    
    with tab2:
        st.subheader("Calories Per Day")
        st.caption("You should not exceed 1430 kcal with no exercise!")
        fig = go.Figure()
        for nutrient in ['calories']:
            fig.add_trace(go.Bar(
                name=nutrient.capitalize(),
                x=df_nutrients.index,
                y=df_nutrients[nutrient],
            ))
            # Add horizontal line at 1430 kcal
            fig.add_hline(y=1430, line_dash="dash", line_color="red", 
                         annotation_text="Daily Limit (1430 kcal)", 
                         annotation_position="top right")
        fig.update_layout(barmode='stack')
        st.plotly_chart(fig)
        
    with tab3:
        st.subheader("Average Macronutrient Ratios")
        avg_nutrients = df_nutrients.mean()
        fig = px.pie(
            values=[avg_nutrients['protein'], avg_nutrients['fat'], avg_nutrients['carbs'], avg_nutrients['fiber']],
            names=['Protein', 'Fat', 'Carbs', 'Fiber'],
            title="Average Daily Macronutrient Distribution"
        )
        st.plotly_chart(fig)       
    
    
    # Summary statistics
    st.subheader("Summary Statistics (Daily Averages)")    
    summary = df_nutrients.mean().round(1)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Calories", f"{summary['calories']:.0f} kcal")
    with col2:
        st.metric("Protein", f"{summary['protein']:.1f}g")
    with col3:
        st.metric("Fat", f"{summary['fat']:.1f}g")
    with col4:
        st.metric("Carbs", f"{summary['carbs']:.1f}g")
    with col5:
        st.metric("Fiber", f"{summary['fiber']:.1f}g")
else:
    st.write("No data available for the selected date range.") 