from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Score, State, Student, ExtendedUser
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

class ExtendedUserForm(ModelForm):
    class Meta:
        model= ExtendedUser
        fields=['phoneNumber', 'user']

class StudentForm(ModelForm):
    class Meta:
        model= Student
        fields=['name', 'rollNo', 'state']

class ScoreForm(ModelForm):
    class Meta:
        model= Score
        fields=['subject', 'marks', 'student']
