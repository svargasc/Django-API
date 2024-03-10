from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from.forms import CreateNewTasks, CreateNewProject
from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.

#Funcion que retorna una respuesta en el navegador
def index(request):
    #importamos o renderizamos el archivo html
    title = "Django course!!"
    return render(request,'index.html', {
        'title': title
    })

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" %username)

# def hello(request, id):
#       print(type(id))
#       return HttpResponse("<h1>Hello %s</h1>" %id)

def about(request): 
    return render(request, 'about.html')

def projects(request):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        #aca le pasamos los projects o datos de la BD o de la clase Projects
        'projects': projects
    })

def tasks(request):
    # task = Task.objects.get(id=id)
    #el get_object_or_404 muestra un page not found
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse("tasks %s" % task.title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form' : CreateNewTasks()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_projects.html', {
            'form': CreateNewProject()
         })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    task = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'projects': project,
        'tasks': task
    })