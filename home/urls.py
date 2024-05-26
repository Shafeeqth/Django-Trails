from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.indexPage, name='home'),
    path('about/', views.aboutPage, name='about'),
    path('booking/', views.bookingPage, name='booking'),
    path('doctors', views.doctorPage, name='doctors'),
    path('contact', views.contactPage, name='contact'),
    path('deppartment', views.deppartmentPage, name='deppartment'),

]