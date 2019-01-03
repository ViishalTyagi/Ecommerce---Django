from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .forms import ContactForm, LoginForm, RegisterForm

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

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    #print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data.get("username")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        #print(request.user.is_authenticated())
        if user is not None:
            #print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("Error")

    return render(request, "auth/login.html", context)


User = get_user_model()
def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data.get("username")
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        new_user  = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/register.html", context)