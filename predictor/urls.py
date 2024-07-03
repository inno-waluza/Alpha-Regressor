# urls.py
from django.urls import path
from .views import HomePageView, PredictPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('predict/', PredictPageView.as_view(), name='predict'),
]
