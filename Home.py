import streamlit as st
from PIL import Image
import os
import re

def home_page():
    st.title(":blue[AI-Based Inventory Optimisation System For Restaurants]")
    
    photo_url = Image.open('resources/Inventory optimisation display.png')
    st.image(photo_url, width=600)
    
    st.markdown("---")
           
    
    st.write("Welcome to the AI-Based Inventory Optimisation application! This application uses machine learning models to predict menu item demand based on various factors such as day of the week, holiday, and weather conditions.")
    
    st.write("To get started, use the sidebar to navigate to different sections of the application.")
    
    st.markdown("---")
    
    st.header("How it Works")
    st.write("1. **Predict Demand:** Enter the day of the week, holiday, and weather condition to predict the menu item that is likely to have high demand.")
    st.write("2. **Optimize Inventory:** Based on the predicted demand, optimise your inventory to ensure sufficient stock of popular menu items and reduce wastage.")
    st.write("3. **Increase Efficiency:** By accurately predicting demand and managing inventory effectively, streamline operations and increase overall efficiency of your restaurant.")
    
    st.markdown("---")
    
    st.header("About the Project")
    st.write("This project leverages machine learning techniques to provide predictive insights into menu item demand, helping restaurant owners optimize their inventory and improve operational efficiency.")
    st.write("Built using Streamlit, Pandas, and scikit-learn, this application demonstrates the power of AI in solving real-world business challenges.")
    
    st.markdown("---")
    
    st.header("Meet the Team")
    st.write("**Mayuresh Harihar**")
    st.write(" **Manas Pandey**")
    st.write(" **Mangesh Raj**")
    st.write(" **Sahil Khangar**")

# Main function to run the Streamlit app
def main():
    home_page()

if __name__ == "__main__":
    main()
