from django.shortcuts import render

# Create your views here.
# urlshort/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .utils import generate_short_url
def home(request):
# Fetch a list of all stored URLs
    urls = URL.objects.all()
    return render(request, 'urlshort/home.html', {'urls': urls})
def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_url = generate_short_url()
        url = URL(long_url=long_url, short_url=short_url)
        url.save()
        return redirect('home')
    return render(request, 'urlshort/shorten_url.html')
def redirect_to_original(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.long_url)
