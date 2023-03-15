from django import forms
from .models import Canhoto

class CanhotoForm(forms.ModelForm):

    class Meta:
        model = Canhoto
        fiels = '__all__'
