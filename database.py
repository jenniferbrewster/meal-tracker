import streamlit as st
import pyodbc
import json
import pandas as pd

def get_connection():
    """Create a connection to Azure SQL Database"""
    conn_str = (
        f"DRIVER={{{st.secrets.azure_sql.driver}}};"
        f"SERVER={st.secrets.azure_sql.server};"
        f"DATABASE={st.secrets.azure_sql.database};"
        f"UID={st.secrets.azure_sql.username};"
        f"PWD={st.secrets.azure_sql.password};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)

def init_database():
    """Create tables if they don't exist"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create recipes table with an ID
    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='recipes' AND xtype='U')
        CREATE TABLE recipes (
            id INT IDENTITY(1,1) PRIMARY KEY,
            recipe_name VARCHAR(255),
            foods NVARCHAR(MAX)
        )
    """)
    
    # Create meals table
    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='meals' AND xtype='U')
        CREATE TABLE meals (
            id INT IDENTITY(1,1) PRIMARY KEY,
            date DATE,
            meal_type VARCHAR(50),
            foods NVARCHAR(MAX)
        )
    """)
    
    conn.commit()
    conn.close()

def save_recipe(recipe_name, foods, recipe_id=None):
    """Save a recipe to the database"""
    conn = get_connection()
    cursor = conn.cursor()
    
    foods_json = json.dumps(foods)
    if recipe_id:
        # Update existing recipe
        cursor.execute("""
            UPDATE recipes
            SET recipe_name = ?, foods = ?
            WHERE id = ?
        """, recipe_name, foods_json, recipe_id)
    else:
        # Insert new recipe
        cursor.execute("""
            INSERT INTO recipes (recipe_name, foods)
            VALUES (?, ?)
        """, recipe_name, foods_json)
    
    conn.commit()
    conn.close()

def delete_recipe(recipe_id):
    """Delete a recipe from the database"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM recipes WHERE id = ?", recipe_id)
    
    conn.commit()
    conn.close()

def load_recipes():
    """Load all recipes from the database"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, recipe_name, foods FROM recipes")
    recipes = []
    for row in cursor.fetchall():
        recipes.append({
            'id': row[0],
            'recipe_name': row[1],
            'foods': json.loads(row[2])
        })
    
    conn.close()
    return recipes

def save_meal(date, meal_type, foods):
    """Save a meal to the database"""
    conn = get_connection()
    cursor = conn.cursor()
    
    foods_json = json.dumps(foods)
    cursor.execute("""
        INSERT INTO meals (date, meal_type, foods)
        VALUES (?, ?, ?)
    """, date, meal_type, foods_json)
    
    conn.commit()
    conn.close()

def load_meals():
    """Load all meals from the database"""
    conn = get_connection()
    
    query = "SELECT id, date, meal_type, foods FROM meals"
    df = pd.read_sql(query, conn)
    
    # Convert id column to regular Python int
    if not df.empty:
        df['id'] = df['id'].astype(int)
    
    conn.close()
    return df

def delete_meal(meal_id):
    """Delete a meal from the database"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Convert meal_id to Python int
    meal_id = int(meal_id)
    
    
    cursor.execute("DELETE FROM meals WHERE id = ?", meal_id)
    
    conn.commit()
    conn.close() 