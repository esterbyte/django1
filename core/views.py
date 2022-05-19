from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Produto

#the mvc or mtv needs the views functions to work
#views django are only created inside aplications, not projects
#views are python functions with parameters (a request) and then returns the request renderization
#passing a template or, a html page, as in line 9 and 13 'index.html' and 'contato.html'
#then we need to create routes to get here and check... we do this on 'urls.py' on our project this time
#index means the home page of a website

def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação Web com Django Framework',
        'produtos': produtos
    }
    return render(request, 'index.html', context)



def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)