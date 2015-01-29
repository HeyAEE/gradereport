from django.db import models

# Create your models here.

class Topic(models.Model):
    ''' A student's performance in a given topic. 
        Unique to the student. '''
    name=models.CharField(max_length=300)
    score=models.FloatField()
    
    def __str__(self):
        return self.name + ": " + str(float(round(self.score*100, 1)))+"%"

class Student(models.Model):
    ''' Representation of a student. First and last name, 
        as well as performance on each subject 
        (normally represented as an array.'''
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    performance=models.ManyToManyField("Topic")
    recently_created=models.BooleanField(default=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    

