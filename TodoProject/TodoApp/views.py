from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import updateForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

class TaskListView(ListView):
    model = Task
    template_name = 'Home.html'
    context_object_name = 'data'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'Details.html'
    context_object_name = 'data'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'Edit.html'
    context_object_name = 'data'
    fields = ('taskName', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('TodoApp:detailview', kwargs={'pk': self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'Delete.html'
    success_url = reverse_lazy('TodoApp:listview')


def home(request):
    detailsObj = Task.objects.all()
    if request.method == 'POST':
        taskName = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = Task(taskName=taskName, priority=priority, date=date)
        task.save()
    return render(request, 'Home.html', {'data': detailsObj})

def deleteTask(request, taskId):
    if request.method == 'POST':
        taskObj = Task.objects.get(id=taskId)
        taskObj.delete()
        return redirect('/')
    return render(request, 'Delete.html')

def updateData(request, taskId):
    taskObj = Task.objects.get(id=taskId)
    formDate = updateForm(request.POST or None, request.FILES, instance=taskObj)
    if formDate.is_valid():
        formDate.save()
        return redirect('/')
    return render(request, 'Update.html', {'form': formDate, 'data': taskObj})
