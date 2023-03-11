from django.shortcuts import render

# Create your views here.


def first_fun(request):
    return render(request, "todo/index.html")