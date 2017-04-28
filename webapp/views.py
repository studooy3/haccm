from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
class BasePageView(TemplateView):
    template_name = "base.html"
    
class ResourcePageView(TemplateView):
    template_name = "resource.html"
class EventPageView(TemplateView):
    template_name = "event.html"
class ContactPageView(TemplateView):
    template_name = "contact.html"
    
class TestPageView(TemplateView):
    template_name = "membership.html"