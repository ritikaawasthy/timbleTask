from django.db import models
from django.contrib.auth.models import User

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(blank=True, unique=True, max_length=12)
    def __str__(self):
        return self.user.username

class State(models.Model):
    name= models.CharField(max_length=400, blank=False)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name


class Student(models.Model):
    name= models.CharField(max_length=400, blank=False)
    rollNo=models.IntegerField(unique= True, blank=False)
    state=models.ManyToManyField(State)
    class Meta:
        ordering = ['rollNo']
        #unique_together = ('name', 'rollNo',)
    def __str__(self):
        return str(self.name) + " | " + str(self.rollNo)

class Score(models.Model):
    subject= models.CharField(max_length=200, blank=False)
    marks= models.IntegerField(blank=False)
    student= models.ForeignKey(to=Student, on_delete=models.CASCADE)
    class Meta:
        ordering = ['student']
        unique_together = ('student', 'subject',)
    def __str__(self):
        return str(self.student.name) +" | "+ str(self.subject)
