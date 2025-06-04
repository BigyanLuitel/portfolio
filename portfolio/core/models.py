from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    

    def __str__(self):
        return self.title

class contact(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    message=models.TextField()
    
    def __str__(self):
        return self.Name
