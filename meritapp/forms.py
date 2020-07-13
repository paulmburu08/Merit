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