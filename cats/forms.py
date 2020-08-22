from django import forms
from . import models


class SearchForm(forms.Form):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    city = forms.CharField(initial="Anywhere")
    name = forms.CharField(initial="Anonymous", required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False)
    appearance = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.Appearance.objects.all()
    )
    is_neutered = forms.BooleanField(required=False)


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        cat = models.Cat.objects.get(pk=pk)
        photo.cat = cat
        photo.save()
