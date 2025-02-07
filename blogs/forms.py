from django import forms
from .models import ArtistProfile

class ArtistProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
        required=False
    )
    profile = forms.ImageField(required=True)
    twitter = forms.URLField(required=False)
    facebook = forms.URLField(required=False)
    instagram = forms.URLField(required=False)

    class Meta:
        model = ArtistProfile
        fields = ['profile', 'bio', 'date_of_birth', 'twitter', 'facebook', 'instagram']
