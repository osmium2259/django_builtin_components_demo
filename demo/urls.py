from django.urls import path
from django.views.generic import TemplateView, FormView
from .views import ContactView

app_name = 'demo'

urlpatterns = [
    path('', TemplateView.as_view(template_name='demo/home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='demo/about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='demo/contact.html'), name='contact'),
]
