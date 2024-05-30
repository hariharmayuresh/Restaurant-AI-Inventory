import streamlit as st
import pandas as pd
import os
import re

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

SALES_DATA_PATH = os.path.join(dir_of_interest, "Demand prediction dataset (Up3).csv")

INVENTORY_DATA_PATH = os.path.join(dir_of_interest, "Inventory dataset(v1).csv")

df_s = pd.read_csv(SALES_DATA_PATH)
df_i = pd.read_csv(INVENTORY_DATA_PATH)

def main():
    
    st.title(':blue[Historical Sales Data]')
    st.write(df_s)
    
    st.markdown("---")
    
    st.title(':blue[Inventory Data]')
    st.write(df_i)
    
    
if __name__ == "__main__":
    main()

