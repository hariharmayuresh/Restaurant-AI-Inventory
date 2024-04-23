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
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "Demand prediction dataset (Up3).csv")

df = pd.read_csv(DATA_PATH)


# Preprocessing
df.rename(columns={'Holiday/Event': 'Holiday'}, inplace=True)
df = df.fillna('NO')
df = df.drop(['Date', 'Quantity Sold', 'Sales Amount (INR)'], axis=1)

X = df[['Day of the week', 'Holiday', 'Weather Condition']]
y = df['Menu Item']

# One-hot encode categorical variables
column_transformer = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(), ['Day of the week', 'Holiday', 'Weather Condition'])
    ],
    remainder='passthrough'
)
X_encoded = column_transformer.fit_transform(X)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Model Selection and Hyperparameter Tuning
model = RandomForestClassifier(random_state=42)
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_

# Model Evaluation
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model accuracy: {accuracy}')

# Save the model and column transformer
joblib.dump(best_model, 'menu_item_prediction_model.joblib')
joblib.dump(column_transformer, 'column_transformer.joblib')

