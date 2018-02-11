from django.forms import ModelForm
from .models import Post
from django import forms


#creating forms from model (modelForm)
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['posts_pub_date','posts_title','posts_text','posts_author']
        widgets = {
            'posts_pub_date': forms.HiddenInput(),
            'posts_title': forms.TextInput(attrs={'placeholder': 'Title', 'id': 'titleField'}),
            'posts_text': forms.Textarea(attrs={'placeholder': 'Your message here', 'id':'textField'}),
            'posts_author': forms.TextInput(attrs={'placeholder': 'Author', 'id':'authorField'})
        }
