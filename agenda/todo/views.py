from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

def index(request):
    todos = Todo.objects.filter(title__contains = request.GET.get('search', ''))
    context = {
        'todos':todos
    }
    return render(request, 'todo/index.html', context)

def create(request):
    if request.method == 'GET':
        form = TodoForm()
        context = {
            'form':form
        }
        return render(request, 'todo/create.html', context)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form':form
        }
        return render(request, 'todo/create.html', context)

def view(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo':todo
    }
    return render(request, 'todo/detail.html', context)

def edit(request, id):
    todo = Todo.objects.get(id=id)
    
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'todo/edit.html', context)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        form.save()
        context = {
            'form':form,
            'id':id
        }
        messages.success(request, 'Profile details updated.')
        return render(request, 'todo/edit.html', context)
        
def delete(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        context = {
            'form':form,
            'id':id
        }
        messages.warning(request, 'Quieres borrar la tarea ?')
        return render(request, 'todo/delete.html', context)
    todo.delete()
    if request.method == 'POST':
        messages.error(request, 'Deleted')
        return redirect('todo')