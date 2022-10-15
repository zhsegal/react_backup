from urllib import request
from django import views
from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from .forms import ContactForm
from .models import ContactModel

class ContactView(CreateView):
    model = ContactModel
    fields = "__all__"
    template_name=  'contact/form.html'
    success_url= "thank-you" 



def thank_you(request):
    return render (request, 'contact/thank-you.html')