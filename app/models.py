from django.db import models

class Student(models.Model):
    name=models.TextField(default=None, max_length=20)
    age=models.TextField(default=None, max_length=20)
    def __str__(self):
        return self.name