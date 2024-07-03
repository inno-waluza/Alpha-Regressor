# urls.py
from django.urls import path
from .views import HomePageView, PredictPageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('predict/', PredictPageView.as_view(), name='predict'),
    path('/about',AboutPageView.as_view(), name='about'),
]
