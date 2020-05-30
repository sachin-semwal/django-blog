from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
            'author':forms.Select(attrs={'class':'form-control textinputclass'}),
            'title':forms.TextInput(attrs={'class':'form-control textinputclass'}),
            'text':forms.Textarea(attrs={'class':'form-control postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
         model = Comment
         fields = ('author','text')

         widgets = {
            'author':forms.TextInput(attrs={'class':'form-control textinputclass'}),
            'text':forms.Textarea(attrs={'class':'form-control postcontent'})
         }
