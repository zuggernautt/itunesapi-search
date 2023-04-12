from django.shortcuts import render
import requests

# Create your views here.

def search(request):
    return render(request, 'search.html')



def results(request):
    query = request.GET.get('query')
    api_url = f'https://itunes.apple.com/search?term={query}&media=music&entity=album'
    response = requests.get(api_url)
    results = response.json()['results']
    return render(request, 'results.html', {'results': results})
