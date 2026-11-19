from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'demo/home.html'


class AboutView(TemplateView):
    template_name = 'demo/about.html'


class ContactView(FormView):
    template_name = 'demo/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('demo:contact')
