from .models import Neighborhood,Profile,Join,Post
from django import forms

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','hood']