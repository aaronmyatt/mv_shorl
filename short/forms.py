from django.forms import ModelForm
from .models import Shorten

class ShortenForm(ModelForm):
    class Meta:
        model = Shorten
        fields = ['url']
