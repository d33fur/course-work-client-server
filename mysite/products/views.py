from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from .database import *

# Create your views here.

def page(request, pageid):
    return HttpResponse(GetTable(pageid))

def products(request, userRequest):
    return HttpResponse(GetProductsByName(userRequest))
def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")