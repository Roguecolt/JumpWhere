from django.shortcuts import render

import requests
# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    if search:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{search}"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        meanings = data[0].get('meanings',[])
        meaning = meanings[0]['definitions'][0]['definition']
        antonyms = meanings[0]['definitions'][0]['antonyms']
        synonyms = meanings[0]['definitions'][0]['synonyms']
        context = {
            'meaning':meaning,
            'antonyms':antonyms,
            'synonyms':synonyms
        }
        return render(request, 'word.html', context)
    
    return render(request, 'index.html')