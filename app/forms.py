from django import forms
from django.forms import ModelForm, Textarea, Select, NumberInput, CheckboxSelectMultiple, NullBooleanSelect,CheckboxInput, MultipleChoiceField, DecimalField
from .models import TypUla, MatkiPszczele, PosiadaneUle, Lokalizacja


#class PosiadaneUleForm(forms.ModelForm):
class PosiadaneUleForm(ModelForm):
    class Meta:
        model = PosiadaneUle
        fields = (
            'miejsce',
            'nazwa',
            'typ_ula',
            'ilosc_ramek',
            'install_date',
            'matka',            
            'matka_date', 
            'aktywny'
            )
        widgets = {
            'miejsce': CheckboxSelectMultiple(),
            'matka': CheckboxSelectMultiple(),
            'typ_ula': CheckboxSelectMultiple(),
            'install_date': NumberInput(attrs={'type':'date'}),
            'matka_date': NumberInput(attrs={'type':'date'}),
            'aktywny': CheckboxInput(),
            'ilosc_ramek': DecimalField(),
        }
 #required = False
 
# class PosiadaneUleForm(forms.Form):




#     #miejsce = forms.ModelMultipleChoiceField(
#         #queryset=Lokalizacja.objects.all(), 
#         #widget=forms.CheckboxSelectMultiple
#         #)
#     nazwa = forms.CharField()
#        # widget=forms.Textarea(
#        #     attrs={
#        #     "placeholder": "podaj nazwe",
#        #     "rows": 1,
#         #    "colws": 1
#         #    }
#         #    ))  
#     #install_date = forms.DecimalField()      
#     #typ_ula = forms.ModelMultipleChoiceField(
#         #queryset=TypUla.objects.all(), 
#         #widget=forms.CheckboxSelectMultiple
#         #)
#     #matka = forms.ModelMultipleChoiceField(
#         #queryset=MatkiPszczele.objects.all(), 
#         #widget=forms.CheckboxSelectMultiple
#        # )
#     #matka_date = forms.DateField() 
#     ilosc_ramek = forms.DecimalField()
#     aktywny = forms.BooleanField(initial = False)
