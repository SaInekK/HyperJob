from django import forms


class CreateVacancy(forms.Form):
    description = forms.CharField(max_length=1024)