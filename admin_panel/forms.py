import imp
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from silk.models import Profile

class UserProfileForm(forms.ModelForm):


    class Meta:
        model = Profile
        fields = ['unit_runs_by','unit_created_at','contact','weekly_target','monthly_target','address','address2','city','zipcode','state']
        widgets = {
        'unit_created_at': forms.DateInput(attrs={'class':'form-control','pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd','type':'date'}),
        }


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1' ,'password2')
