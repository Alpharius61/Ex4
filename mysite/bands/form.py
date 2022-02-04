from django import forms
from bands.models import BandsManage


class bandForm(forms.ModelForm):

    class Meta:
        model = BandsManage
        fields = ['name', 'Actif', 'Type']