from django import forms
from .models import Profile,Project

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','creat_date']
        widgets = {
            'number' : forms.TextInput(),
            'email' : forms.EmailInput(),
            'address' : forms.TextInput()
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','post_date','profile']
        widgets = {
            'title' : forms.TextInput(),
            'link' : forms.TextInput(),
            'technologies' : forms.Textarea(),
            'collaborators' : forms.Textarea()
        }