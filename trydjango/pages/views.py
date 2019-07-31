from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello, world!</h1>")
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "things to contact me with",
        "my_number": 123,
        "my_list": [112, 322, 333, 4344, 'ABC']
    }
    return render(request, 'contact.html', my_context)