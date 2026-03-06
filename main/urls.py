from django.urls import path
from .views import index, services, docshel, about, contacts

urlpatterns = [
    path('', index, name='index'),
    path('services/', services, name='services'),
    path('docshel/', docshel, name='docshel'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
]
