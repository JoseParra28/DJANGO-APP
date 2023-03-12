from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.


def first_fun(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "todo/index.html", context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('first_fun')
        form = ItemForm()
        context = {
            'form': form
        }
    return render(request, "todo/add_item.html")

