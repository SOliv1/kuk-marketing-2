from django.urls import path
from . import views


urlpatterns = [
    path('', views.video),
    path('', views.video, name='video'),

]
