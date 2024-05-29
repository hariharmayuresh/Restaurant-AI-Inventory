import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from itertools import combinations
import os

# Define paths to data and models
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
dir_of_models = os.path.join(PARENT_DIR, "models")

INGREDIENTS_DATA_PATH = os.path.join(dir_of_interest, "Ingredients(v1).csv")
INVENTORY_DATA_PATH = os.path.join(dir_of_interest, "Inventory dataset(v1).csv")
MENU_DATA_PATH = os.path.join(dir_of_models, "menu_item_prediction_model.joblib")
COLUMN_DATA_PATH = os.path.join(dir_of_models, "column_transformer.joblib")

# Load the trained model and column transformer
model = joblib.load(MENU_DATA_PATH)
column_transformer = joblib.load(COLUMN_DATA_PATH)

# Load the datasets
inventory_df = pd.read_csv(INVENTORY_DATA_PATH)
ingredient_df = pd.read_csv(INGREDIENTS_DATA_PATH)

# Ensure the ingredients are in a consistent order
ingredient_df['Ingredients'] = ingredient_df.apply(lambda x: ', '.join(sorted([x['Ingredient_1'], x['Ingredient_2']])), axis=1)

# Prepare the data
X = ingredient_df['Ingredients']
y = ingredient_df['Menu Item']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and train the recommendation model
models = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', RandomForestClassifier(random_state=42))
])
models.fit(X_train, y_train)

# Function to predict menu items from inventory
def predict_menu_items():
    available_ingredients = inventory_df['Ingredient Name'].unique().tolist()
    # Generate all possible combinations of two ingredients
    ingredient_combinations = list(combinations(available_ingredients, 2))
    # Sort each combination to ensure consistency
    sorted_combinations = [', '.join(sorted(combo)) for combo in ingredient_combinations]
    predictions = models.predict(sorted_combinations)
    return set(predictions)

# Predict all possible menu items from inventory
predicted_menu_items = predict_menu_items()

# Function to process user inputs and predict top menu items
def process(day, holiday, weather):
    input_data = pd.DataFrame({'Day of the week': [day], 'Holiday': [holiday], 'Weather Condition': [weather]})
    input_data_transformed = column_transformer.transform(input_data)
    predictions = model.predict_proba(input_data_transformed)
    top_two_indices =predictions[0].argsort()[-3:][::-1]
    #top_two_indices = predictions[0].argsort()[-2:][::-1]  # Get indices of top 2 predictions
    return model.classes_[top_two_indices]

# Create Streamlit app
def main():
    st.title("Menu Item Demand Prediction")

    # User inputs
    day = st.selectbox("Day of the Week:", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    holiday = st.selectbox("Holiday:", ["New Year's Day", 'NO', 'Weekend', 'Pongal', 'Makar Sankranti', 'Republic Day', "Valentine's Day", 'Holi', 'Gudi Padwa', "April Fools' Day", 'Ram Navami', 'Good Friday', 'Easter Sunday', 'Ambedkar Jayanti', 'Hanuman Jayanti', 'Buddha Purnima', 'May Day', "Mother's Day", 'Eid al-Fitr', "Father's Day", 'Bakri Id', 'Raksha Bandhan', 'Janmashtami', 'Independence Day','Ganesh Chaturthi', 'Onam', 'Hindi Diwas', 'Navratri'])
    weather = st.selectbox("Weather Condition:", ['Clear', 'Foggy', 'Rainy'])
    
    # Predict top two menu items based on user inputs
    top_two_menu_items = process(day, holiday, weather)
    
    if st.button("Demand Prediction"):
        st.header(f"Predicted Menu Items: {top_two_menu_items[0]}, {top_two_menu_items[1]},{top_two_menu_items[2]}")
    st.markdown("---")

    # Find common items between in-demand predictions and possible menu items
    set_menu_items = set(top_two_menu_items)
    recommended_items = set_menu_items.intersection(predicted_menu_items)
    recommended_items_str = ', '.join(recommended_items)
    
    if st.button("Recommendation Module"):
        st.title("Menu Item Recommendation Based on Current Inventory and Demand Prediction")
        
    if st.button("Recommend Menu Items"):
        st.subheader(f"Demand Predicted Menu Items: {top_two_menu_items[0]}, {top_two_menu_items[1]}, {top_two_menu_items[2]}")
        
        if recommended_items:
            st.header("Recommended Menu Items  (Based on current Inventory):")
            st.subheader(recommended_items_str)
        else:
            st.write("No Recommendation based on current inventory and Demand Prediction.")
        
    st.markdown("---")
            
    if st.button("Predict All Possible Menu Items based on Current Inventory"):
        st.title("All Possible Menu Items based on Current Inventory")
        st.table(predicted_menu_items)

if __name__ == "__main__":
    main()