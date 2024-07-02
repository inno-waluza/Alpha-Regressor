from django.views.generic import TemplateView
from django.shortcuts import render
##import pandas as pd
from .forms import HouseForm
from .utils.model_loader import load_model_and_pipeline

class home_page(TemplateView):
    template_name = 'home.html'

class predict_page(TemplateView):
    template_name = 'prediction.html'

    def get(self, request, *args, **kwargs):
        form = HouseForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = HouseForm(request.POST)
        if form.is_valid():
            # Process form data
            longitude = form.cleaned_data['longitude']
            latitude = form.cleaned_data['latitude']
            housing_median_age = form.cleaned_data['housing_median_age']
            total_rooms = form.cleaned_data['total_rooms']
            total_bedrooms = form.cleaned_data['total_bedrooms']
            population = form.cleaned_data['population']
            households = form.cleaned_data['households']
            median_income = form.cleaned_data['median_income']
            ocean_proximity = form.cleaned_data['ocean_proximity']

            # Load the model and pipeline
            model, pipeline = load_model_and_pipeline()

            # Prepare the data for prediction
            input_data = pd.DataFrame([[
                longitude, latitude, housing_median_age, total_rooms,
                total_bedrooms, population, households, median_income, ocean_proximity
            ]], columns=[
                'longitude', 'latitude', 'housing_median_age', 'total_rooms',
                'total_bedrooms', 'population', 'households', 'median_income', 'ocean_proximity'
            ])

            # Transform the data using the pipeline
            transformed_data = pipeline.transform(input_data)

            # Make the prediction
            predicted_price = model.predict(transformed_data)[0]

            # Render the prediction result page with data
            return render(request, 'prediction.html', {
                'longitude': longitude,
                'latitude': latitude,
                'housing_median_age': housing_median_age,
                'total_rooms': total_rooms,
                'total_bedrooms': total_bedrooms,
                'population': population,
                'households': households,
                'median_income': median_income,
                'ocean_proximity': ocean_proximity,
                'predicted_price': predicted_price
            })
        else:
            # If form is not valid, render the prediction page with the form and errors
            return render(request, 'prediction.html', {'form': form, 'errors': form.errors})
