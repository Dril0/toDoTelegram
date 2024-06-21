from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Create your views here.


@login_required
def task_list(request):
    """filtra y muestra una lista de tareas del usuario autenticado en el html task_list"""
    tasks = Task.objects.filter(user=request.user)
    return render(request, "todo/task_list.html", {"tasks": tasks})


@login_required
def task_detail(request, pk):
    """muestra los detalles de la tarea especificada utilizando el pk  renderizado en el html task_detail, sino devuelve un error 404"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, "todo/task_detail.html", {"task": task})


@login_required
def task_create(request):
    """permite crear una tarea, si es post la valida y guiarda asociada al usuario actual, si es GET mueztra un formulario vacio para crear una tarea, lo renderiza en el html task_form"""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_detail", pk=task.pk)
    else:
        form = TaskForm()
    return render(request, "todo/task_create.html", {"form": form})


@login_required
def task_update(request, pk):
    """actualiza una tarea especificada por el pk, guardandola si es POST la renderizaa en task_list y mostrando los datos de la tarea si es GET, se renderiza en la pagina task_create"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_detail", pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, "todo/task_create.html", {"form": form})


@login_required
def task_delete(request, pk):
    """nos permite eliminar una tarea"""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "todo/task_confirm_delete.html", {"task": task})
