from django import forms
from store.models import Comment
class NameForm(forms.Form):
    name = forms.CharField(max_length=150)
    subject=forms.CharField(max_length=150)
    email=forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']
