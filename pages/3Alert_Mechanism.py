import streamlit as st
import pandas as pd
import os
import re

# Load the inventory data
# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "Inventory dataset(v1).csv")
INVENTORY_DATA_PATH = os.path.join(dir_of_interest, "Inventory dataset(v1).csv")
df_i = pd.read_csv(INVENTORY_DATA_PATH)

st.title("Inventory Alert Mechanism")
st.header('Inventory Data')
st.write(df_i)

# Load the inventory data
inventory_data = {
    'Ingredient Name': ['Assorted Dishes', 'Assorted Vegetables', 'Bread', 'Carrots', 'Cashews', 'Chicken', 'Chickpea Flour (Besan)', 'Chickpeas', 'Coconut', 'Eggplant', 'Eggs', 'Fish', 'Flour', 'Kidney Beans', 'Kulfi', 'Lentils', 'Maida (Refined Wheat Flour)', 'Mango', 'Milk', 'Mixed Vegetables', 'Moong Dal (Green Gram)', 'Mutton', 'Noodles', 'Okra', 'Paneer', 'Potato', 'Rice and Lentil Batter', 'Semolina (Sooji)', 'Spinach', 'Tea Leaves', 'Various Chutneys', 'Vegetables', 'Wheat Flour', 'Yogurt', 'Butter', 'Cauliflower', 'Cream', 'Curry Paste or Powder', 'Falooda Sev (Vermicelli)', 'Ghee (Clarified Butter)', 'Korma Sauce', 'Masala (Spice Mix)', 'Meat or Vegetables', 'Nuts and Spices', 'Paan Leaves', 'Pav (Bread)', 'Pistachios', 'Rice or Bread', 'Saffron', 'Spices', 'Spring Roll Wrappers', 'Sugar', 'Sugar Syrup', 'Tamarind Chutney', 'Tandoori Masala', 'Yeast or Baking Powder'],
    'Quantity': [100, 150, 200, 50, 80, 120, 90, 100, 70, 60, 30, 80, 100, 50, 40, 60, 75, 30, 200, 120, 70, 90, 80, 60, 100, 50, 100, 60, 40, 30, 60, 100, 80, 150, 50, 70, 100, 40, 30, 50, 40, 60, 90, 80, 30, 120, 40, 100, 20, 70, 50, 150, 40, 30, 60, 30],
    'Used By': ['30 days', '7 days', '5 days', '10 days', '30 days', '3 days', '60 days', '90 days', '14 days', '7 days', '14 days', '3 days', '30 days', '60 days', '30 days', '90 days', '60 days', '7 days', '5 days', '7 days', '90 days', '3 days', '60 days', '7 days', '14 days', '30 days', '14 days', '90 days', '7 days', '30 days', '14 days', '7 days', '60 days', '7 days', '14 days', '7 days', '14 days', '30 days', '60 days', '30 days', '14 days', '30 days', '3 days', '30 days', '14 days', '5 days', '30 days', '5 days', '60 days', '30 days', '60 days', '30 days', '14 days', '30 days', '90 days']
}
inventory_df = pd.read_csv(DATA_PATH)

# Streamlit app
st.header("Check your Inventory")

# Dropdown to select ingredient name
ingredient_name = st.selectbox("Select Ingredient Name:", inventory_df['Ingredient Name'])

# Numeric input for current quantity
current_quantity = st.number_input("Enter Current Quantity:", min_value=0, value=0, step=1)

# Button to check inventory and generate alert
if st.button("Check Inventory"):
    # Get the threshold quantity (25% of the listed quantity)
    threshold_quantity = inventory_df[inventory_df['Ingredient Name'] == ingredient_name]['Quantity'].values[0] * 0.25
    
    # Get the 'Used By' information
    used_by = inventory_df[inventory_df['Ingredient Name'] == ingredient_name]['Used By'].values[0]
    
    # Check if current quantity is below the threshold
    if current_quantity < threshold_quantity:
        st.error(f"Alert: Inventory for {ingredient_name} is below the threshold at {current_quantity} units. Threshold is {threshold_quantity} units.")
    else:
        st.success(f"Inventory level for {ingredient_name} is above the threshold. Threshold is {threshold_quantity} units.")
    
    # Display 'Used By' information
    st.write(f"Used By: {used_by}")