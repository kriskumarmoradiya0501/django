from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    hobbies = models.CharField(max_length=200)
    language = models.CharField(max_length=20)
    gujarati = models.IntegerField()
    english = models.IntegerField()

    def __str__(self):
        return self.name