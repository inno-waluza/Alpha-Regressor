# predictor/urls.py

from django.urls import path
from .views import home_page, predict_page

urlpatterns = [
    path('', home_page.as_view(), name='home'),  # Set a name for the URL pattern
     path('predict/', predict_page.as_view(), name='predict'),
]