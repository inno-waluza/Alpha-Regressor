from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import HouseForm 

class home_page(TemplateView):
    template_name = 'home.html'

class  predict_page(TemplateView):
    template_name = 'prediction.html'

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
            Some computations will be here
            """
            return render(request, 'prediction.html', {
                'longitude': longitude,
                'latitude': latitude,
                'housing_median_age': housing_median_age,
                'total_rooms': total_rooms,
                'total_bedrooms': total_bedrooms,
                'population': population,
                'households': households,
                'median_income': median_income,
                'ocean_proximity': ocean_proximity
            })

        return render(request, 'prediction.html', {'form': form})  # Render the form with errors if form is not valid
