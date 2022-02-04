from django import forms
from listings.models import Listing


class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ['name', 'description', 'price', 'listing_type', 'band']
