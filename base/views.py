from django.shortcuts import render
from dummy_objects.models import Article, Product

def home_page(request):
    context = {
        'articles': Article.objects.all(),
        'products': Product.objects.all(),
        'favorites_list': request.session.get('favorites'),
    }

    return render(request, 'base/base.html', context)
