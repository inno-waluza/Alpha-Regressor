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

    def clean(self):
        cleaned_data = super().clean()

        longitude = cleaned_data.get('longitude')
        latitude = cleaned_data.get('latitude')
        """
        housing_median_age = cleaned_data.get('housing_median_age')
        total_rooms = cleaned_data.get('total_rooms')
        total_bedrooms = cleaned_data.get('total_bedrooms')
        median_income = cleaned_data.get('median_income')
        """

        if longitude < -180 or longitude > 180:
            self.add_error('longitude', 'Longitude must be between -180 qnd 180')

        if latitude < -90 or latitude > 90:
            self.add_error('latitude', 'Latitude must be between -90 and 90')

        return cleaned_data
