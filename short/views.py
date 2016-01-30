from django.shortcuts import HttpResponse, render_to_response
from .forms import ShortenForm

# Create your views here.

def url_encode(request):
    if request.method == 'POST':
        return HttpResponse()

    # GET

    return render_to_response('shorten.html', context={'form':ShortenForm()})

def url_decode(request, pattern):
    return HttpResponse()
