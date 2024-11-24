from django import forms


class BloggerRegistrationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )
    login = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Write a short description about yourself!'})
    )
    blog_category = forms.ChoiceField(
        choices=[('travel', 'Travel'), ('lifestyle',
                                        'Lifestyle'), ('food', 'Food'), ('gaming', 'Gaming')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class BloggerLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
