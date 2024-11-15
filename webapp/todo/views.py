from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()

            all_items = List.objects.all
            messages.success(request, ('Item added'))
            return render(request, 'home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def about(request):
    context = {"fname": "Jhon", "lname": "Jhonson"}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item was deleted'))
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    messages.success(request, ('Item status changed'))
    return redirect('home')

def cross_on(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    messages.success(request, ('Item status changed'))
    return redirect('home')

def edit_todo(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()

            all_items = List.objects.all
            messages.success(request, ('Item has been edited'))
            return render(request, 'home.html', {'all_items': all_items})

    else:
        todo = List.objects.get(pk=list_id)
        return render(request, 'todo.html', {'todo': todo})
