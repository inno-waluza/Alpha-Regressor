# model_loader.py
import joblib
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import os

# Custom transformer for attribute combination
class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        rooms_per_household = X[:, 3] / X[:, 6]
        population_per_household = X[:, 5] / X[:, 6]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, 4] / X[:, 3]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

# Get current file directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute paths for the model and pipeline files
model_path = os.path.join(BASE_DIR, "house_price_model.pkl")
pipeline_path = os.path.join(BASE_DIR, "full_pipeline.pkl")

# Load the saved model and pipeline using the constructed paths
# Use the __main__ module to help the pickler find the CombinedAttributesAdder class
import __main__
__main__.CombinedAttributesAdder = CombinedAttributesAdder

final_model = joblib.load(model_path)
full_pipeline = joblib.load(pipeline_path)

def predict_house_price(input_data):
    new_data = pd.DataFrame([input_data])
    prepared_data = full_pipeline.transform(new_data)
    predictions = final_model.predict(prepared_data)
    return predictions[0]

# Example usage
if __name__ == "__main__":
    example_data = {
        'longitude': -122.23,
        'latitude': 37.88,
        'housing_median_age': 41.0,
        'total_rooms': 880.0,
        'total_bedrooms': 129.0,
        'population': 322.0,
        'households': 126.0,
        'median_income': 8.3252,
        'ocean_proximity': 'NEAR BAY'
    }

    prediction = predict_house_price(example_data)
    print(f"Predicted house price: {prediction}")
