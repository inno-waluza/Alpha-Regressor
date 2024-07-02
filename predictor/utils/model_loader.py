import joblib
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# Define the CombinedAttributesAdder class
class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):  # no *args or **kwargs
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  # nothing else to do

    def transform(self, X):
        rooms_per_household = X[:, 3] / X[:, 6]
        population_per_household = X[:, 5] / X[:, 6]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, 4] / X[:, 3]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

# Load the model and pipeline
def load_model_and_pipeline():
    model = joblib.load('house_price_model.pkl')
    pipeline = joblib.load('full_pipeline.pkl')
    return model, pipeline

# Function to predict house prices
def predict_house_price(input_data):
    model, pipeline = load_model_and_pipeline()
    
    # Convert input_data to DataFrame if it's not already
    if not isinstance(input_data, pd.DataFrame):
        input_data = pd.DataFrame(input_data, columns=['longitude', 'latitude', 'housing_median_age', 
                                                       'total_rooms', 'total_bedrooms', 'population', 
                                                       'households', 'median_income', 'ocean_proximity'])

    prepared_data = pipeline.transform(input_data)
    predictions = model.predict(prepared_data)
    return predictions

if __name__ == "__main__":
    # Dummy input data
    new_data = pd.DataFrame({
        'longitude': [-122.23],
        'latitude': [37.88],
        'housing_median_age': [41.0],
        'total_rooms': [880.0],
        'total_bedrooms': [129.0],
        'population': [322.0],
        'households': [126.0],
        'median_income': [8.3252],
        'ocean_proximity': ['NEAR BAY']
    })

    # Convert DataFrame to numpy array for prediction
    example_data = new_data.values

    # Predict house prices
    predictions = predict_house_price(example_data)
    print("Predicted house prices:", predictions)
