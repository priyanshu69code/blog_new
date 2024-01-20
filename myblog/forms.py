from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Enter The Post Title'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Enter The Post Title'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
