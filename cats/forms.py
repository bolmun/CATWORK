from django import forms
from . import models


class SearchForm(forms.Form):

    name = forms.CharField(initial="Anywhere")
    city = forms.CharField(initial="Anywhere")
    gender = forms.CharField(required=False)
