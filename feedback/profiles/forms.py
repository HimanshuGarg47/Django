from django import forms

class ProfileForm(forms.Form):
    image = forms.ImageField(label="Upload here")