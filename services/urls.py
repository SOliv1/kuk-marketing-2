from django.urls import path
from . import views


urlpatterns = [

    path('services/about', views.about, name='about'),
    path('services/our_brands', views.our_brands, name='our_brands'),
    path('services/about_us', views.about_us, name='about_us'),
    path('services/brands', views.brands, name='brands'),
    path('services/contact', views.contact, name='contact'),



]