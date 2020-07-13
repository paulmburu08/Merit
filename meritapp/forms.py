from django import forms
from .models import Profile,Project

class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        exclude = ['user','creat_date']
        widgets = {
            'number' : forms.TextInput(),
            'email' : forms.EmailInput(),
            'address' : forms.TextInput()
        }

class ProjectForm(forms.Form):
    class Meta:
        model = Project
        exclude = ['user','post_date','profile']
        widgets = {
            'title' : forms.TextInput(),
            'link' : forms.TextInput(),
            'technologies' : forms.Textarea(),
            'collaborators' : forms.Textarea()
        }