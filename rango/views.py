from django.shortcuts import render
from rango.models import Page
from rango.forms import CategoryForm

from django.http import HttpResponse

# Import the Category model 
from rango.models import Category, Page

# Created a view called index
# Return HttpResponse object, which takes a String parameter
#representing the conent of the page we wish to send to the
#client requesting the view 
def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'categories': category_list, 'pages': page_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict) 
    #return HttpResponse("Rango says hey there partner!")


def about(request):
    context_dict = {'bold': "want to know more about cats?"}
    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        # Note that filter() returns a list of page objects or an empty list
        pages = Page.objects.filter(category=category)
        
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.        
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None


    # create a default query based on the category name
    # to be shown in the search box
    context_dict['query'] = category.name

    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run our Webhose function to get the results list!
            result_list = run_query(query)
            context_dict['query'] = query
    context_dict['result_list'] = result_list


    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)


 def add_category(request):
    form = CategoryForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But instead since the most recent catergory added is on the index page
            # Then we can direct the user back to the index page.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    # Will handle the bad form (or form details), new form or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})   
    
