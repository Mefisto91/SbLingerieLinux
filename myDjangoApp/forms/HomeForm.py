from django import forms
from models.HomeModel import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

