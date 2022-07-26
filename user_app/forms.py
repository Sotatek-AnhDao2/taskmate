import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

class NewUserForm(UserCreationForm):
   email = forms.EmailField(required=True)
   first_name=forms.CharField(required=False)
   last_name=forms.CharField(required=False)
   birth_day=forms.DateField(required=False)
    
   class Meta:
      model = User
      fields = ("username","first_name","last_name","birth_day","email", "password1", "password2")
   def save(self,commit=True):
       user = super(NewUserForm, self).save(commit=False)
       user.email = self.cleaned_data['email']
       if commit:
          user.save()
       return user
      

    