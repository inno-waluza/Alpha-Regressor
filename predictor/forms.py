from django import forms

# Define choices for ocean proximity
OCEAN_PROXIMITY_CHOICES = [
    ('<1H OCEAN', '<1H OCEAN'),
    ('INLAND', 'INLAND'),
    ('NEAR OCEAN', 'NEAR OCEAN'),
    ('NEAR BAY', 'NEAR BAY'),
    ('ISLAND', 'ISLAND'),
]

class HouseForm(forms.Form):
    longitude = forms.FloatField(label='Longitude', required=True)
    latitude = forms.FloatField(label='Latitude', required=True)
    housing_median_age = forms.FloatField(label='Housing Median Age', required=True)
    total_rooms = forms.IntegerField(label='Total Rooms', required=True)
    total_bedrooms = forms.IntegerField(label='Total Bedrooms', required=True)
    population = forms.IntegerField(label='Population', required=True)
    households = forms.IntegerField(label='Households', required=True)
    median_income = forms.FloatField(label='Median Income', required=True)
    ocean_proximity = forms.ChoiceField(label='Ocean Proximity', choices=OCEAN_PROXIMITY_CHOICES, required=True)

    #input data validation
    def clean(self):
        cleaned_data = super().clean()

        longitude = cleaned_data.get('longitude')
        latitude = cleaned_data.get('latitude')
        median_income = cleaned_data.get('median_income')
        total_bedrooms = cleaned_data.get('total_bedrooms')
        housing_median_age = cleaned_data.get('housing_median_age')
        total_rooms = cleaned_data.get('total_rooms')

        if longitude < -180 or longitude > 180:
            self.add_error('longitude', 'Longitude must be between -180 qnd 180')
        if latitude < -90 or latitude > 90:
            self.add_error('latitude', 'Latitude must be between -90 and 90')
        if median_income < 10 :
            self.add_error('median_income', 'Median income must atlest be 10')
        if total_bedrooms < 1 :
            self.add_error('total_bedrooms', 'Number of bedrooms must atleast be 1')
        if housing_median_age < 1:
            self.add_error('housing_median_age', "Housing median age can't be 0")
        if total_rooms < total_bedrooms :
            self.add_error('total_rooms', "Total rooms can't be less than total bedrooms")
        if total_rooms < 1:
            self.add_error('total_rooms', "Total rooms should atlest be 1")
        return cleaned_data
