from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<str:name>/contact/', 
        views.contact_success_message, 
        name='contact_success_message'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
]