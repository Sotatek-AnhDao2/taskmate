from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TaskList
class TaskForm(forms.ModelForm):
    class Meta:
        model=TaskList
        fields=["task","done"]
