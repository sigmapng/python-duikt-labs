from django import forms
from .models import Blogger


class BloggerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Blogger
        fields = ['name', 'category', 'description', 'social_links']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'social_links': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        category = cleaned_data.get('category')

        if not name:
            self.add_error('name', 'This field is required.')

        if not category:
            self.add_error('category', 'This field is required.')
        return cleaned_data


class BloggerLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
