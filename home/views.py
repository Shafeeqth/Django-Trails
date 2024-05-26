from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPage(request):

    

    return render(request, 'index.html')
def aboutPage(request):
    person = {
        'name' : 'shafeeque',
        'age' : 23,
        'place' : 'Kalikavu'
    }
    return render(request, 'about.html',person)
def bookingPage(request):
    Numbers = {
        'Lst' : [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, 'booking.html',Numbers)
def doctorPage(request):
    my_string = {
        'My' : 'is my string which is a string'
    }
    return render(request, 'doctors.html',my_string)
def contactPage(request):
    return render(request, 'contact.html')
def deppartmentPage(request):
    return render(request, 'deppartment.html')