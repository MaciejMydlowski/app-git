from django import forms

from .models import Przeglad, DodawanieUla, TypUla

class PostForm(forms.ModelForm):

    class Meta:
        model = Przeglad
        fields = ('title', 'text',)

class UlForm(forms.ModelForm):
    class Meta:
        model = DodawanieUla
        fields = ('nazwa', 'matka', 'typ_ula','install_date')
        
