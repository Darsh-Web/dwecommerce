from django.urls import path
from . import views
from .views import contact_view, support_oem, oem_contact_view,terms_view, privacy_view
urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('home_contact/', views.home_contact, name='home_contact'),
    path("contact/", contact_view, name="contact"),
    path('faq/', views.faq, name='faq'),
    path('products/', views.products, name='products'),
    path('support-oem/', support_oem, name='support_oem'),
    path('oem-contact/', oem_contact_view, name='oem_contact'),
    path('terms/', terms_view, name='terms'),
    path('privacy/', privacy_view, name='privacy'),
]
