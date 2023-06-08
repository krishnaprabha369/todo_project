from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . models import Task
from . forms import TodoForm



# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        slnum = request.POST.get('slnum','')
        name = request.POST.get('name','')
        desc = request.POST.get('desc','')
        task = Task(slnum=slnum,name=name,desc=desc)
        task.save()

    return render(request,'home.html',{'task1':task1})

def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,taskid):
    task = get_object_or_404(Task,id=taskid)
    if request.method == 'POST':
        task.slnum = request.POST.get('slnum')
        task.name = request.POST.get('name')
        task.desc = request.POST.get('desc')
        task.save()
        return redirect('/')

    return render(request,'edit.html',{'task':task})
        
   