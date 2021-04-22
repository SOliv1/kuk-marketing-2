from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages 
# from .services import forms


"""view-link to return our services menu on main-nav bar"""


def about_us(request):
    """ A view to our services page """

    return render(request, 'services/about_us.html')


def brands(request):
    """ A view to brands page """

    return render(request, 'services/brands.html')


def about(request):
    """ view to return the about page """

    return render(request, 'services/about.html')


def our_brands(request):
    """ A view to our_brands page """

    return render(request, 'services/our_brands.html')


def contact(request, methods=["GET", "POST"]):
    """ A view to contact us page """
    request.GET

    return render(request, 'services/contact.html')

    """ view-link to return about us menu on main-nav bar"""


def graphic_design(request):
    """ A view to graphic design page """

    return render(request, 'services/graphic_design.html')


def web_design(request):
    """ A view to web design page """

    return render(request, 'services/web_design.html')







