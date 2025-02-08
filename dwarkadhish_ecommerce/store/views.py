from django.shortcuts import render

def home(request):
    # Example data, you can replace this with real model data
    products = [
        {"name": "Laptop", "price": "₹50,000"},
        {"name": "Smartphone", "price": "₹30,000"},
        {"name": "Monitor", "price": "₹15,000"},
    ]

    return render(request, 'store/home.html', {'products': products})
from django.shortcuts import render

def about(request):
    return render(request, 'store/about.html')

def services(request):
    return render(request, 'store/services.html')

def contact(request):
    return render(request, 'store/contact.html')

def faq(request):
    return render(request, 'store/faq.html')
# views.py


from .models import Product

def products(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'store/products.html', {'products': products})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)
        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")

    return render(request, "store/contact.html")

def home_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Validate email & phone number
        if not email or not phone:
            messages.error(request, "Email and Phone Number are required.")
            return redirect("home")  # Redirect back to home page

        if not phone.isdigit() or len(phone) != 10:
            messages.error(request, "Enter a valid 10-digit phone number.")
            return redirect("home")

        # Save contact form data
        Contact.objects.create(name=name, email=email, phone=phone, subject="Home Page Contact", message=message)

        messages.success(request, "Your message has been sent successfully!")
        return redirect("home")

    return redirect("home")


from .models import OEMInquiry

def support_oem(request):
    return render(request, "store/support_oem.html")

def oem_contact_view(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        contact_name = request.POST.get("contact_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        gem_registered = request.POST.get("gem_registered")
        gem_category = request.POST.get("gem_category", "")
        products_services = request.POST.get("products_services")
        website = request.POST.get("website", "")
        additional_info = request.POST.get("additional_info", "")

        OEMInquiry.objects.create(
            company_name=company_name,
            contact_name=contact_name,
            email=email,
            phone=phone,
            gem_registered=gem_registered,
            gem_category=gem_category if gem_registered == "Yes" else "",
            products_services=products_services,
            website=website,
            additional_info=additional_info
        )

        messages.success(request, "Your inquiry has been submitted successfully!")
        return redirect("support_oem")

    return render(request, "store/support_oem.html")

def terms_view(request):
    return render(request, 'store/terms.html')

def privacy_view(request):
    return render(request, 'store/privacy.html')