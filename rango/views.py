from django.shortcuts import render

from django.http import HttpResponse

# Created a view called index
# Return HttpResponse object, which takes a String parameter
#representing the conent of the page we wish to send to the
#client requesting the view 
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict) 
    #return HttpResponse("Rango says hey there partner!")


def about(request):
    context_dict = {'bold': "want to know more about cats?"}
    return render(request, 'rango/about.html', context=context_dict)

