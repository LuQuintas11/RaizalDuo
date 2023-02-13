from .models import Comment
from django import forms
from django.forms import ModelForm, Textarea


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('body',)


class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, 
          **kwargs)
        self.fields['body'].widget.attrs.update(
          {'class': 'form-control'})
    class Meta:
        model = Comment
        fields = ['body']    
        widgets = {
            'text': Textarea(attrs={'rows': 4}),
        }