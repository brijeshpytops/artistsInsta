from django import forms
from .models import ArtistProfile

class ArtistProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), 
        required=False
    )
    profile = forms.ImageField(
        required=True, 
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    twitter = forms.URLField(
        required=False, 
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Twitter URL'})
    )
    facebook = forms.URLField(
        required=False, 
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Facebook URL'})
    )
    instagram = forms.URLField(
        required=False, 
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Instagram URL'})
    )

    class Meta:
        model = ArtistProfile
        fields = ['profile', 'bio', 'date_of_birth', 'twitter', 'facebook', 'instagram']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter bio'}),
        }
