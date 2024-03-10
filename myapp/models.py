from django.db import models

# Create your models here.

#creamos clases para guardar los datos o tablas que vamos a usar en la DB

class Project(models.Model):
    name = models.CharField(max_length=200)

    #mostar nombre de los projects en el admin
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    #mostar nombre de las tasks en el admin
    def __str__(self):
        return self.title + " - " + self.project.name