from django.urls import path
from . import views

urlpatterns = [    
    path("",views.ContactView.as_view()),
    path ("thank-you", views.thank_you)
]