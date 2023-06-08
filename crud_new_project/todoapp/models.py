from django.db import models

# Create your models here.
class Task(models.Model):
    slnum = models.IntegerField()
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=200)
    
    def __str__(self):
        return self.name
