from django.shortcuts import render

from django.http import HttpResponse

# Created a view called index
# Return HttpResponse object, which takes a String parameter
#representing the conent of the page we wish to send to the
#client requesting the view 
def index(request):
    return HttpResponse("Rango says hey there partner!") 
