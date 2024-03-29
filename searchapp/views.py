from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .search import search, sorting  # relative import
import json

# renders the search page.


def search_view(request):
    return render(request, 'search.html', {})

# Returns the autocomplete results while the user types in a letter.


def search_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get('term', '')
        results = sorting(search(query.lower()), query.lower())
        data = json.dumps(results)
    else:
        data = 'fail'
    type = 'application/json'
    return HttpResponse(data, type)

# Returns a Json response having the search results(25 words) containing the searched word(partial)


def getSearchResults(request):
    if request.method == 'GET':
        query = request.GET.get('term')  # for example: query = 'hello'
        if query:
            searchresult = sorting(search(query.lower()), query.lower())
            if len(searchresult) == 0:
                return JsonResponse({'Search_Result': "Word not found."})
            else:
                return JsonResponse({'Search_Result': searchresult})
        else:
            return redirect('/')
