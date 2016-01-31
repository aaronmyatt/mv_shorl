from django.shortcuts import HttpResponse, render_to_response, render
from .forms import ShortenForm
from .models import Shorten

# Create your views here.

def url_encode(request):
    user = request.user

    if request.method == 'POST':
        form = ShortenForm(request.POST)

        if form.is_valid():
            original = form.cleaned_data['url']
            short = Shorten(
                user=user,
                url=original
            )
            short.save()

            render(request, template_name='shorten.html',
                   context={'form':ShortenForm(),
                            'url':original,
                            'code':'code',
                            "previous":Shorten.objects.filter(user=user)
                            }
                   )

    # GET
    previous = Shorten.objects.filter(user=user)
    return render(request, 'shorten.html',
                  context={
                      'form':ShortenForm(),
                      'previous':previous}
                  )

def url_decode(request, pattern):
    return HttpResponse()
