from django.urls import path
from . import views


urlpatterns = [

    path('services/about_us', views.about_us, name='about_us'),
    path('services/why_kensington_fields', views.why_kensington_fields, name='why_kensington_fields'),
    path('services/contact', views.contact, name='contact'),

]