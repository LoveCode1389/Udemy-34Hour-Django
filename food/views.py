from django.shortcuts import render,redirect
from django.http import HttpResponse
from food.forms import ItemForm
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
    context = {
        'email': 'erfankhajehzadhe@gmail.com',
        'phone' : '0212345678',
    }
    return render(request, 'food/contact.html', context)

def create_food(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html',{
        'form': form,
    })

def update_food(request, id):
    food = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=food)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {
        'form':form,
        'food':food,
        })

def delete_food(request, id):
    food = Item.objects.get(id=id)

    if request.method == 'POST':
        food.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {
        'food': food,
    })
