from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    course = models.CharField()
    
    def __str__(self):
        return self.name