from django.shortcuts import render
from django.views import View
from predictor.forms import HouseForm
from predictor.utils.model_loader import predict_house_price

class HomePageView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class AboutPageView(View):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class PredictPageView(View):
    template_name = 'prediction.html'
    form_class = HouseForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            input_data = {
                'longitude': form.cleaned_data['longitude'],
                'latitude': form.cleaned_data['latitude'],
                'housing_median_age': form.cleaned_data['housing_median_age'],
                'total_rooms': form.cleaned_data['total_rooms'],
                'total_bedrooms': form.cleaned_data['total_bedrooms'],
                'population': form.cleaned_data['population'],
                'households': form.cleaned_data['households'],
                'median_income': form.cleaned_data['median_income'],
                'ocean_proximity': form.cleaned_data['ocean_proximity']
            }

            predicted_price = predict_house_price(input_data)
            predicted_price= round(predicted_price, 2)
            predicted_price = "${:,.2f}".format(predicted_price)

            return render(request, self.template_name, {
                'form': form,
                'predicted_price': predicted_price,
                'longitude': form.cleaned_data['longitude'],
                'latitude': form.cleaned_data['latitude'],
                'housing_median_age': form.cleaned_data['housing_median_age'],
                'total_rooms': form.cleaned_data['total_rooms'],
                'total_bedrooms': form.cleaned_data['total_bedrooms'],
                'population': form.cleaned_data['population'],
                'households': form.cleaned_data['households'],
                'median_income': form.cleaned_data['median_income'],
                'ocean_proximity': form.cleaned_data['ocean_proximity']
            })
        else:
            return render(request, self.template_name, {'form': form})