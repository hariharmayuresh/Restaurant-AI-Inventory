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
inventory_df = pd.read_csv(DATA_PATH)

st.title(":blue[Inventory Alert Mechanism]")
st.header('Inventory Data')
st.write(inventory_df)

st.markdown("---")

# Streamlit app
st.header("Check your Inventory")

# Dropdown to select ingredient name
ingredient_name = st.selectbox("**Select Ingredient Name:**", inventory_df['Ingredient Name'])

# Numeric input for current quantity used
current_quantity_used = st.number_input("**Enter Quantity Used:**", min_value=0, value=0, step=1)

# Display 'Used By' information
used_by = inventory_df[inventory_df['Ingredient Name'] == ingredient_name]['Used By'].values[0]

# Button to check inventory and generate alert
if st.button("**:green-background[:green[Update Inventory]]**"):
    # Get the current inventory quantity
    current_inventory_quantity = inventory_df[inventory_df['Ingredient Name'] == ingredient_name]['Quantity'].values[0]
    
    # Calculate the remaining quantity after use
    remaining_quantity = current_inventory_quantity - current_quantity_used
    
    # Get the threshold quantity (25% of the listed quantity)
    threshold_quantity = current_inventory_quantity * 0.25
    
    
    
    # Check if remaining quantity is below the threshold
    if remaining_quantity < threshold_quantity:
        # st.error(f"Alert: Inventory for {ingredient_name} is below the threshold at {remaining_quantity} units. Threshold is {threshold_quantity} units.")
        st.error(f"**:red[Alert: Inventory for {ingredient_name} is below the threshold at {remaining_quantity} units.]**")
        st.error(f"**:red[Threshold is {threshold_quantity} units.]**")
        st.error(f"**:red[Used By: {used_by}]**")
    else:
        #st.success(f"Inventory level for {ingredient_name} is above the threshold. Remaining quantity is {remaining_quantity} units. Threshold is {threshold_quantity} units.")
        st.success(f"**:green[Inventory level for {ingredient_name} is above the threshold.]**")
        st.success(f"**:green[Remaining quantity is {remaining_quantity} units.]**") 
        st.success(f"**:green[Threshold is {threshold_quantity} units.]**")   
        st.success(f"**:green[Used By: {used_by}]**")
    # Display 'Used By' information
    # used_by = inventory_df[inventory_df['Ingredient Name'] == ingredient_name]['Used By'].values[0]
    # st.success(f"Used By: {used_by}")