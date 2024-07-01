from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import HouseForm

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

            """
            Perform any additional computations or predictions here
            """

            # Assuming you have a function to predict house price
            #predicted_price = predict_house_price(longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, ocean_proximity)

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
            })
        else:
            # If form is not valid, render the prediction page with the form and errors
            return render(request, 'prediction.html', {'form': form})
