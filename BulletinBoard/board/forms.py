from django import forms
from django.forms import ModelForm

from .models import Post, Response
from ckeditor.widgets import CKEditorWidget


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'files', 'category']
        content = forms.CharField(widget=CKEditorWidget, label='')


class RespForm(ModelForm):
    class Meta:
        model = Response
        fields = ['text']


class AcceptForm(ModelForm):
    class Meta:
        model = Response
        fields = ['status']

