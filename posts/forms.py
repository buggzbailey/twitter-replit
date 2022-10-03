from django import forms
from django.forms import fields
from .models import Post
from django.forms import ModelForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'body', 'image']
