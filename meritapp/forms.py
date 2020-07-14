from django import forms
from .models import Profile,Project,Ratings

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','creat_date']
        widgets = {
            'name' : forms.TextInput(),
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

DESIGN = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
]

USABILITY = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
]

CONTENT = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
]

class RateForm(forms.ModelForm):
    design = forms.ChoiceField(choices=DESIGN, widget=forms.RadioSelect())
    usability = forms.ChoiceField(choices=USABILITY, widget=forms.RadioSelect())
    content = forms.ChoiceField(choices=CONTENT, widget=forms.RadioSelect())

    class Meta:
        model = Ratings
        exclude = ['project' ,'user' , 'average']
        fields = ['design' , 'usability', 'content']