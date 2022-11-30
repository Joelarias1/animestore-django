from django import forms
from django.forms import ModelForm 
from .models import contactUs



class newCommentForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your last name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your Email"}))
    comment = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Comment"}))
    class Meta:
        model = contactUs
        exclude = ['']