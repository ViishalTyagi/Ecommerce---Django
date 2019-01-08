from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .forms import ContactForm

def home(request):
    context = {
        "title":"Allu!",
        "content":" Redefining your shopping experience.",
        "premium_content": "Welcome! Discover, Engage & Shop Fashion apparel using Allu's hyperlocal product.",
    }
    # if request.user.is_authenticated():
    #     context["premium_content"] = "Welcome! Discover, Engage & Shop Fashion apparel using Allu's hyperlocal product."
    return render(request, "home.html", context)

def about(request):
    context = {
        "title":"About Us:",
        "content":""" 
                    Allu is a Hyperlocal Fashion application which lets the user discover and engage with NYC's phenomenal fashion sector including Boutique Shops, Multi-branded outlets. 
                    We aren't an E-Commerce application but we believe in Real Commerce. 
                    Allu is aimed to solve the pitfalls or disadvantages of both Online and Retail Shopping primarily in Fashion apparel sector.
                """
    }
    return render(request, "about.html", context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "content":" Contact Us ",
        "form": contact_form,
    }
        
    return render(request, "contact.html", context)