from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTodoForm, EditTodoForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . models import Todo

def index(request):
    query = request.GET.get('query', '')
    todos = Todo.objects.all()
    
    if query:
        todos = todos.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    context = {
        'todos': todos,
        'query': query
    }
    return render(request, 'todoApp/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
        return redirect('todoApp:index')
    else:
        form = SignUpForm()
    
    context = {
        'form': form
    }
    return render(request, 'todoApp/signup.html', context)

@login_required
def createTodo(request):
    if request.method == 'POST':
        form = NewTodoForm(request.POST)
        
        if form.is_valid():
            newTodo = form.save(commit=False)
            # Add Authentication before saving
            newTodo.created_by = request.user
            newTodo.save()
            
            return redirect('todoApp:index')
        
    else:
        form = NewTodoForm()
        
        
    context = {
        'form': form
    }
    
    return render(request, 'todoApp/form.html', context)

@login_required
def editTodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditTodoForm(request.POST, instance=todo)
        
        if form.is_valid():
            form.save()
            
            return redirect('todoApp:index')
    else:
        form = EditTodoForm(instance=todo)
        
    context = {
        'form': form,
    }
    
    return render(request, 'todoApp/form.html', context)

@login_required
def deleteTodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, created_by=request.user)
    todo.delete()
    
    return redirect('todoApp:index')
        
    