from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
    foods = Item.objects.all()

    context = {
        "foods": foods,
    }
    return render(request,'food/index.html', context)

def item(request):
    return HttpResponse("<h1 style='text-align: center;'>This is an item view</h1>")

def detail(request, id):
    food = Item.objects.get(pk=id)
    context = {
        'food': food,
    }

    return render(request, 'food/detail.html', context)

def contact(request):
    return render(request, 'food/contact.html')
