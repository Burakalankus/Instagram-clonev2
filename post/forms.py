from django import forms
from .models import Post , Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['image', 'caption', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Yorumunuzu buraya girin...'}),
        }
        labels = {
            'content': '',
        }