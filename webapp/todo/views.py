from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    context = {"fname": "Jhon", "lname":"Jhonson"}
    return render(request, 'about.html', context)
