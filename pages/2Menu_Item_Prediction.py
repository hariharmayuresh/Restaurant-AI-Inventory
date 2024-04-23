import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, classification_report
import joblib
from PIL import Image
import os
import re

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "models")

MENU_DATA_PATH = os.path.join(dir_of_interest, "menu_item_prediction_model.joblib")
COLUMN_DATA_PATH = os.path.join(dir_of_interest, "column_transformer.joblib")

# Load the trained model and column transformer
model = joblib.load(MENU_DATA_PATH)
column_transformer = joblib.load(COLUMN_DATA_PATH)

# Create Streamlit app
def main():
    st.title("Menu Item Demand Prediction")

    # User inputs
    day = st.selectbox("Day of the Week:", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    holiday = st.selectbox("Holiday:", ["New Year's Day", 'NO', 'Weekend', 'Pongal', 'Makar Sankranti', 'Republic Day', "Valentine's Day", 'Holi', 'Gudi Padwa', "April Fools' Day", 'Ram Navami', 'Good Friday', 'Easter Sunday', 'Ambedkar Jayanti', 'Hanuman Jayanti', 'Buddha Purnima', 'May Day', "Mother's Day", 'Eid al-Fitr', "Father's Day", 'Bakri Id', 'Raksha Bandhan', 'Janmashtami', 'Independence Day','Ganesh Chaturthi', 'Onam', 'Hindi Diwas', 'Navratri'])
    weather = st.selectbox("Weather Condition:", ['Clear', 'Foggy', 'Rainy'])

    if st.button("Predict"):
        input_data = pd.DataFrame({'Day of the week': [day], 'Holiday': [holiday], 'Weather Condition': [weather]})
        input_data_transformed = column_transformer.transform(input_data)
        predictions = model.predict_proba(input_data_transformed)
        top_two_indices = predictions[0].argsort()[-2:][::-1]  # Get indices of top 2 predictions
        top_two_menu_items = model.classes_[top_two_indices]
        st.header(f"Predicted Menu Items: {top_two_menu_items[0]}, {top_two_menu_items[1]}")
        
if __name__ == "__main__":
    main()