from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item

# Create your views here.

def index(response, id):
    ls = TodoList.objects.get(id=id)
    #item = ls.item_set.get(id=1)
    return render(response, 'main/list.html', {"ls":ls})

def home(response):
    return render(response, 'main/home.html', {})
