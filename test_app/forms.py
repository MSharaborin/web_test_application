from django import forms
from .models import Signalling


class AddSignalling(forms.ModelForm):
    class Meta:
        model = Signalling
        fields = ('type', 'address', 'latitude', 'longitude', 'coverage_area',)
