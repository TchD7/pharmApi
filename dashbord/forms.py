from django.forms import ModelForm
from django import forms
from .models import Pharms


class PharmForm(ModelForm):
    '''name = forms.CharField()
    description = forms.CharField()
    localisation = forms.URLField()
    commune = forms.ChoiceField()'''

    class Meta:
        model = Pharms
        fields = '__all__'
        #fields = ('name', 'description', 'localisation', 'commune')
