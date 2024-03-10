from django.urls import path
from . import views

#configuracion de las rutas para el navegador
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<int:id>', views.hello, name="hello"),
    path('hello/<str:username>', views.hello, name="hellou"),
    path('project_detail/<int:id>', views.project_detail, name="project_detail"),
    path('projects/', views.projects, name="projects"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
]