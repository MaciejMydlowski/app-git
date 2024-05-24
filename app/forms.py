from django import forms

from .models import Przeglad

class PostForm(forms.ModelForm):

    class Meta:
        model = Przeglad
        fields = ('title', 'text',)
