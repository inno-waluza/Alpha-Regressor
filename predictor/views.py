
from django.views import View
from django.views.generic import TemplateView

class home_page(TemplateView):
    template_name = 'home.html'

class predict_page(TemplateView):
    template_name = 'prediction.html'