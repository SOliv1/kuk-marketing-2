from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages 
from . models import Contact
# from .services import forms


"""view-link to return our services menu on main-nav bar"""


def about_us(request):
    """ A view to our services page """

    return render(request, 'services/about_us.html')


def why_kensington_fields(request):
    """ A view to why-kensington-fields page """

    return render(request, 'services/why_kensington_fields.html')


def contact(request, methods=["GET", "POST"]):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        package_type=request.POST.get('package_type')
        description=request.POST.get('description')
        print(name, email, package_type, description)
        contact = Contact(name=name, email=email, package_type=package_type, description=description)
        contact.save()
        messages.info(request, 'Thanks for contacting!')
        return render(request, 'services/contact.html')
    else:
        return render(request, 'services/contact.html')

    """ view-link to return about us menu on main-nav bar"""









