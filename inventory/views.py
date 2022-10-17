from django.shortcuts import render
from .models import *


def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Product.objects.filter(name__contains=query_name)
            return render(request, 'homepage/product_search.html', {"results":results})

    return render(request, 'homepage/product_search.html')