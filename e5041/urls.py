from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('politika/', TemplateView.as_view(template_name='politika.html'), name='politika'),
    path('soglasie/', TemplateView.as_view(template_name='soglasie.html'), name='soglasie'),
]
