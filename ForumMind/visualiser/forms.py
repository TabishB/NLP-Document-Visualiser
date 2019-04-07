from django import forms
from crispy_forms.helper import FormHelper

from visualiser.models import *

class DocumentForm(forms.ModelForm):
    class Meta:
        model = FileDoc
        fields = ('topics','document',)
