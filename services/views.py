from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages 
# from .services import forms


"""view-link to return our services menu on main-nav bar"""


def about_us(request):
    """ A view to our services page """

    return render(request, 'services/about_us.html')


def why_kensington_fields(request):
    """ A view to why-kensington-fields page """

    return render(request, 'services/why_kensington_fields.html')


def contact(request, methods=["GET", "POST"]):
    """ A view to contact us page """
    request.GET

    return render(request, 'services/contact.html')

    """ view-link to return about us menu on main-nav bar"""









