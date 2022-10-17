from django.shortcuts import render, redirect
from .models import Mytodo
from .forms import TodoForm 
# Create your views here.
def alltodos(request):
    task = Mytodo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'alltodo.html', {'task':task, 'form': form})


def deleteItem(request, pk):
    task = Mytodo.objects.get(id = pk)
    task.delete()
    return redirect('alltodos')


def updateItem(request, pk):
    task = Mytodo.objects.get(id = pk)
    updateForm = TodoForm(instance = task)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance = task)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('alltodos')
    return render(request, 'updateItem.html', {'task':task, 'updateForm':updateForm})
    
    

