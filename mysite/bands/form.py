from django import forms
from bands.models import BandsAdd



class bandForm(forms.ModelForm):
    class Meta:
        model = BandsAdd
        fields = ['name', 'active','description', 'bands_type']
